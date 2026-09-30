

import pygame

def run( maze, grid_height, grid_width, cell_size, CELL_COLOURS ):
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode( (grid_width * cell_size, grid_height * cell_size) )

    def draw_maze( ):
            for x in range( grid_width ):
                for y in range( grid_height ):
                    colour = CELL_COLOURS[ maze[y][x] ]
                    pygame.draw.rect( screen, colour, (x * cell_size, y * cell_size, cell_size, cell_size) )

        
    running = True
        
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        draw_maze()
        
        pygame.display.flip()
        
        clock.tick(60)
        
    pygame.quit()