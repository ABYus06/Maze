
import pygame
import random
from enum import IntEnum

# Declare the directions
DIRECTIONS = [ (0, 2), (2, 0), (0, -2), (-2, 0) ]

class Cell( IntEnum ):
    WALL = 0
    PATH = 1
    START = 2
    END = 3

CELL_COLOURS = {
    Cell.WALL: (100, 100, 100),
    Cell.PATH: (0, 0, 0),
    Cell.START: (255, 0, 0),
    Cell.END: (0, 255, 0),
}

class MazeClass:
    def __init__( self, grid_height, grid_width, cell_size ):

        if grid_height % 2 == 0: 
            grid_height += 1

        if grid_width % 2 == 0: 
            grid_width += 1

        self.grid_height = grid_height
        self.grid_width = grid_width
        self.cell_size = cell_size

        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode( (grid_width * cell_size, grid_height * cell_size) )

        self.maze = None
        self.path = None
        self.start_point = None
        self.end_point = None


    # Check if the next cell will be in bounds
    def check_bounds( self, x, y ):
        if 0 <= x < self.grid_width and 0 <= y < self.grid_height:
            return True
        else:
            return False


    # Iterative DFS to create the maze path
    def depth_first_search( self, x, y ):
        stack = [(x, y)]
        self.maze[y][x] = Cell.PATH

        while stack:
            current_x, current_y = stack[ -1 ]

            directions = DIRECTIONS.copy()
            random.shuffle( directions )

            for direction_x, direction_y in directions:
                next_x = current_x + direction_x
                next_y = current_y + direction_y

                # Check if the destination inside the maze
                if not self.check_bounds( next_x, next_y ):
                    continue
                
                # Check if this cell has already been visited
                if self.maze[ next_y ][ next_x ] != Cell.WALL:
                    continue

                self.maze[ (current_y + direction_y // 2) ][ (current_x + direction_x // 2) ] = Cell.PATH
                self.maze[ next_y ][ next_x ] = Cell.PATH
                stack.append( (next_x, next_y) )   
                break

            else:
                stack.pop()   


    # Create the start and end point of the maze
    def select_end_and_start_points( self ):

        for x in range( self.grid_width ):
            for y in range( self.grid_height ):
                if self.maze[y][x] == Cell.PATH:
                    self.path.append( (x, y) )

        # Choose the start point
        self.start_point = random.choice( self.path )
        self.maze[ self.start_point[1] ][ self.start_point[0] ] = Cell.START
    
        # Choose the end point
        self.end_point = random.choice( self.path )
        while self.end_point == self.start_point:
            self.end_point = random.choice( self.path )
        self.maze[ self.end_point[1] ][ self.end_point[0] ] = Cell.END
        

    def create_maze_layout(self):

        self.maze = [ [Cell.WALL for _ in range(self.grid_width)] for _ in range(self.grid_height) ]
        self.path = []

        self.depth_first_search(1, 1)
        self.select_end_and_start_points()

        return self.maze, self.path, self.start_point, self.end_point

   
    def draw_maze( self ):
        cell_size = self.cell_size

        for x in range( self.grid_width ):
            for y in range( self.grid_height ):
                colour = CELL_COLOURS[ self.maze[y][x] ]
                pygame.draw.rect( self.screen, colour, (x * cell_size, y * cell_size, cell_size, cell_size) )


    def run(self):

        self.create_maze_layout()

        running = True

        while running:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False

            self.draw_maze()

            pygame.display.flip()

            self.clock.tick(60)

        pygame.quit()
