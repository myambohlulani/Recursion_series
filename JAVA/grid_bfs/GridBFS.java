package grid_bfs;

import java.util.*;

public class GridBFS {
    // right down left up
    int[][] directions = { { 0, 1 }, { 1, 0 }, { 0, -1 }, { -1, 0 } };

    // grid
    public void bfsGrid(int[][] grid, int starX, int starY) {
        int rows = grid.length;
        int cols = grid[0].length;
        boolean[][] visited = new boolean[rows][cols];
        Queue<int[]> queue = new LinkedList<>();

        queue.offer(new int[] { starX, starY });
        visited[starX][starY] = true;

        while (!queue.isEmpty()) {
            int[] current = queue.poll();
            int x = current[0];
            int y = current[1];

            System.out.printf("Visiting: %i, %i.%n", x, y);

            for (int[] dir : directions) {
                int newX = x + dir[0];
                int newY = y + dir[1];
                if (newX >= 0 && newY >= 0 && rows > newX && cols > newY && !visited[newX][newY]
                        && grid[newX][newY] == 1) {
                    visited[newX][newY] = true;
                    queue.offer(new int[] { newX, newY });
                }
            }
        }
    }
}
