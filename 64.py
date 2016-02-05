class Solution(object):
    def minPathSum(self, grid):
        if (not grid) or (not grid[0]): return 0

        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                elif i > 0 and j == 0:
                    grid[i][0] += grid[i - 1][0]
                elif i == 0 and j > 0:
                    grid[0][j] += grid[0][j - 1]
                else:
                    grid[i][j] += min(grid[i][j - 1], grid[i - 1][j])

        return grid[m - 1][n - 1]
