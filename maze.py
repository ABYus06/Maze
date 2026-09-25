
import pygame
import random

WINDOW_SIZE = (510, 510)
WALL_COLOUR = (100, 100, 100)
PATH_COLOUR = (0, 0, 0)
START_TILE_COLOUR = (255, 0, 0)
END_TILE_COLOUR = (0, 255, 0)

CELL_SIZE = 10
GRID_WIDTH = int(WINDOW_SIZE[0] / CELL_SIZE)
GRID_HEIGHT = int(WINDOW_SIZE[1] / CELL_SIZE)

WALL = "#"
PATH = "."
START = "~"
END = "£"

# Declare the directions
DIRECTIONS = [(0, 2), (2, 0), (0, -2), (-2, 0)]


class MazeClass:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        self.clock = pygame.time.Clock()

        self.maze = [[WALL for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

    # Check if the next cell will be in bounds
    def CheckBounds( self, x, y ):
        if 0 <= x < GRID_WIDTH and 0 <= y < GRID_HEIGHT:
            return True
        else:
            return False
        
    # Recursive DFS to create the maze path
    def DepthFirstSearch(self, x, y):
        
        self.maze[y][x] = PATH

        directions = DIRECTIONS.copy()
        random.shuffle( directions )

        for direction_x, direction_y in directions:
            next_x = x + direction_x
            next_y = y + direction_y

            # Check if the destination inside the maze
            if not self.CheckBounds( next_x, next_y):
                continue

            # Check if this cell has already been visited
            if self.maze[next_y][next_x] != WALL:
                continue

            self.maze[y + direction_y // 2][x + direction_x // 2 ] = PATH
            self.DepthFirstSearch( next_x, next_y )

    # Create the start and end point of the maze
    def SelectEndAndStartPoints(self):

        def CheckIfValid( sp, ep ):
            return sp != ep

        path = []

        for x in range(GRID_WIDTH):
            for y in range(GRID_HEIGHT):
                if self.maze[y][x] == PATH:
                    path.append((y,x))

        # Choose the start point
        start_point = random.choice( path )

        print(path)

        self.maze[start_point[1]][start_point[0]] = START
    
        # Choose the end point
        end_point = random.choice( path )
        if ( CheckIfValid ):
            self.maze[end_point[1]][end_point[0]] = END
        



    def CreateMazeLayout(self):

        self.DepthFirstSearch(1, 1)
        self.SelectEndAndStartPoints()

        """
        # Print out the maze layout in the terminal
        for row in self.maze:
            print(''.join(row))
        """


    def DrawMaze(self):
        for x in range(GRID_WIDTH):
            for y in range(GRID_HEIGHT):
                if self.maze[y][x] == WALL:
                    pygame.draw.rect(self.screen, WALL_COLOUR, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                elif self.maze[y][x] == PATH:
                    pygame.draw.rect(self.screen, PATH_COLOUR, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                elif self.maze[y][x] == START:
                    pygame.draw.rect(self.screen, START_TILE_COLOUR, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                elif self.maze[y][x] == END:
                    pygame.draw.rect(self.screen, END_TILE_COLOUR, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

                


    def Run(self):

        self.CreateMazeLayout()

        running = True

        while running:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill(PATH_COLOUR)

            self.DrawMaze()

            pygame.display.flip()

            self.clock.tick(60)

        pygame.quit()
