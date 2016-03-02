class Solution:
    def wallsAndGates(self, rooms):
        if not rooms: return

        from collections import deque
        queue = deque([])

        m, n = len(rooms), len(rooms[0])
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue.append((i, j))
        dircs = ((0, 1), (0, -1), (1, 0), (-1, 0))
        while queue:
            x, y = queue.popleft()
            for dirc in dircs:
                next_x, next_y = x + dirc[0], y + dirc[1]
                if next_x < 0 or next_x >= m or next_y < 0 or next_y >= n or rooms[next_x][next_y] != 2147483647:
                    continue
                rooms[next_x][next_y] = rooms[x][y] + 1
                queue.append((next_x, next_y))