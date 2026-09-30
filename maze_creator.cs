using System;
using System.Collections.Generic;

using random;

// Declare the directions
int[,] DIRECTIONS = new int[,]
{
    (0, 2),
    (2, 0),
    (0, -2),
    (-2, 0) 
};

public static class Shuffler<T>
{
    private static Random random = new Random();

    public static T[] Shuffle(T[] array)
        {
        int n = array.Length;
        for (int i = 0; i < n; i++)
        {
            int r = i + random.Next(n - i);
            T temp = array[r];
            array[r] = array[i];
            array[i] = temp;
        }
        return array;
    }
}

// Create the Cell class
public class CellClass
{
    enum CellTypes
    {
        Wall = 0,
        Path = 1,
        Start = 2,
        End = 3,
    }

    ( string CellType, int Colour )[] CELL_COLOURS = new ( string, int )[]
    {
        CellClass.CellTypes.Wall = (100, 100, 100),
        CellClass.CellTypes.Path = (0, 0, 0),
        CellClass.CellTypes.Start = (255, 0, 0),
        CellClass.CellTypes.End = (0, 255, 0),
    };
}

public class MazeClass
{
    private int gridWidth;
    private int gridHeight;
    private int cellSize;

    public int[,] maze = null;
    public int[,] path = null;
    public int[,] startPoint = null;
    public int[,] endPoint = null;
    public MazeClass( int gridWidth, int gridHeight, int cellSize )
    {
        if ( gridWidth % 2 == 0 )
        {
            gridWidth += 1;
        }
        if ( gridHeight % 2 == 0 )
        {
            gridHeight += 1;
        }

        gridWidth = gridWidth;
        gridHeight = gridHeight;
        cellSize = cellSize;
    }

    // Check if the next cell will be in bounds
    public CheckBounds( int x, int y )
    {
        if ( 0 <= x < this.gridWidth && 0 <= y < this.gridHeight )
            return true;
        return false;
    }

    // Iterative DFS to create the maze path
    public DepthFirstSearch( int x, int y )
    {
        Stack<int> currentCell = new Stack<int>();
        this.maze[x][y] = CellClass.CellTypes.Path;

        while ( currentCell )
        {
            ( currentX, currentY ) = currentCell[ -1 ];

            int[,] shuffledDirections = new int[,];
            Array.Copy(DIRECTIONS, 0, shuffledDirections, 0, source.Length);
            Shuffler<int>.Shuffle(shuffledDirections);

            foreach ( int (directionX, directionY) in shuffledDirections )
            {
                int nextX = currentX + directionX;
                int nextY = currentY + directionY;
            }

            // Check if the destination is within the bounds of the maze
            if ( MazeClass.CheckBounds( nextX, nextY ) == false )
            {
                continue;
            }

            // Check if the next cell has not already been visited
            if ( this.maze[nextX][nextY] != CellClass.CellTypes.Wall )
            {
                continue;
            }

            this.maze[ (currentX + directionX / 2) ][ (currentY + directionY / 2) ] = CellClass.CellTypes.Path;
            this.maze[ nextX ][ nextY ] = CellClass.CellTypes.Path;
            currentCell.Push((nextX, nextY));
            break;
        }
        currentCell.Pop();
    }

    public CreateMazeLayout()
    {
        // Create the maze full of walls
        Cell[,] maze = new Cell[gridHeight, gridWidth];

        for (int i = 0; i < gridHeight; i++)
        {
            for (int j = 0; j < gridWidth; j++)
            {
                maze[i, j] = Cell.WALL;
            }
        }

        MazeClass.DepthFirstSearch(1, 1);
    }
}

class Program
{
    static void Main()
    {
        MazeClass.CreateMazeLayout();
    }
}