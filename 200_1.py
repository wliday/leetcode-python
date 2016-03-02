class Solution(object):
    def numIslands(self, grid):
        if not grid or not grid[0]: return 0
        
        dircs = ((0, 1), (0, -1), (1, 0), (-1, 0))
        def dfs(i, j):
            grid[i][j] = 'x'
            for dirc in dircs:
                next_i, next_j = i + dirc[0], j + dirc[1]
                if next_i < 0 or next_i >= m or next_j < 0 or next_j >= n or grid[next_i][next_j] != '1':
                    continue
                dfs(next_i, next_j)
        
        m, n = len(grid), len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i, j)

                    res += 1
        return res