from maze_creator import MazeClass
from maze_renderer import run

if __name__ == "__main__":
    maze = MazeClass( 50, 50, 10 )
    maze_layout, path, start_point, end_point, cell_colours = maze.create_maze_layout()
    run( maze_layout, maze.grid_height, maze.grid_width, maze.cell_size, cell_colours )
