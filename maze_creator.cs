using System;
using System.Linq;
using System.Collections.Generic;

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


public enum CellTypes
{
    Wall = 0,
    Path = 1,
    Start = 2,
    End = 3,
}

public class MazeClass
{
    // Declare the directions
    private static ( int directionX, int directionY )[] DIRECTIONS =
    {
        (0, 2),
        (2, 0),
        (0, -2),
        (-2, 0) 
    };


    private int gridWidth;
    private int gridHeight;
    private int cellSize;

    private Random random = new Random();

    public CellTypes[,] maze = null;
    public CellTypes[,] path = null;
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

        this.gridWidth = gridWidth;
        this.gridHeight = gridHeight;
        this.cellSize = cellSize;

        this.maze = new CellTypes[gridHeight, gridWidth];

    }

    // Check if the next cell will be in bounds
    public bool CheckBounds( int x, int y )
    {
        if ( x >= 0 && x < this.gridWidth && y >= 0 && y < this.gridHeight )
        {
            return true;
        }
        return false;
    }

    // Iterative DFS to create the maze path
    public void DepthFirstSearch( int x, int y )
    {
        Stack<(int x, int y)> currentCell = new Stack<(int x, int y)>();
        this.maze[x, y] = CellTypes.Path;
        currentCell.Push((x, y));

        while ( currentCell.Count > 0 )
        {
            bool moved = false;

            var (currentX, currentY) = currentCell.Peek();
            var shuffledDirections = DIRECTIONS.ToArray();
            Shuffler<(int directionX, int directionY)>.Shuffle(shuffledDirections);

            foreach ( var (directionX, directionY) in shuffledDirections )
            {
                int nextX = currentX + directionX;
                int nextY = currentY + directionY;

                // Check if the destination is within the bounds of the maze
                if ( CheckBounds( nextX, nextY ) == false )
                {
                    continue;
                }

                // Check if the next cell has not already been visited
                if ( this.maze[nextX, nextY] != CellTypes.Wall )
                {
                    continue;
                }

                this.maze[ (currentX + directionX / 2), (currentY + directionY / 2) ] = CellTypes.Path;
                this.maze[ nextX, nextY ] = CellTypes.Path;
                currentCell.Push((nextX, nextY));
                moved = true;
                break;
            }

            if ( moved == false )
            {
                currentCell.Pop();
            }
        }
    }

    public void CreateMazeLayout()
    {
        // Create the maze full of walls
        for (int y = 0; y < gridHeight; y++)
        {
            for (int x = 0; x < gridWidth; x++)
            {
                this.maze[y, x] = CellTypes.Wall;
            }
        }

        this.DepthFirstSearch(1, 1);
    }

    public void PrintMaze()
    {
        for (int y = 0; y < gridHeight; y++)
        {
            for (int x = 0; x < gridWidth; x++)
            {
                if (maze[y, x] == CellTypes.Wall)
                {
                    Console.Write("##");
                }
                else
                {
                    Console.Write("  ");
                }
            }

            Console.WriteLine();
        }
    }

}

class Program
{
    static void Main()
    {
        MazeClass maze = new MazeClass(51, 51, 10);
        maze.CreateMazeLayout();
        maze.PrintMaze();
    }
}