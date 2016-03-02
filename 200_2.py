class Solution(object):
    def numIslands(self, grid):
        if not grid or not grid[0]: return 0

        dircs = ((0, 1), (0, -1), (1, 0), (-1, 0))

        m, n = len(grid), len(grid[0])
        res = 0
        from collections import deque
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    queue = deque([])
                    queue.append((i, j))
                    while queue:
                        x, y = queue.popleft()
                        if grid[x][y] == 'x':
                            continue
                        grid[x][y] = 'x'
                        for dirc in dircs:
                            next_x, next_y = x + dirc[0], y + dirc[1]
                            if next_x < 0 or next_x >= m or next_y < 0 or next_y >= n or grid[next_x][next_y] != '1':
                                continue
                            queue.append((next_x, next_y))
                    res += 1

        return res