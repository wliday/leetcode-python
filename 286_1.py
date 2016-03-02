class Solution:
    def wallsAndGates(self, rooms):
        if not rooms: return

        m, n = len(rooms), len(rooms[0])
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    self.dfs(rooms, m, n, i, j)

    def dfs(self, rooms, m, n, i, j):
        dircs = ((0, -1), (0, 1), (1, 0), (-1, 0))
        for dirc in dircs:
            next_i, next_j = i + dirc[0], j + dirc[1]
            if next_i >= m or next_i < 0 or next_j >= n or next_j < 0 or rooms[next_i][next_j] == -1:
                continue
            if rooms[next_i][next_j] > rooms[i][j] + 1:
                rooms[next_i][next_j] = rooms[i][j] + 1
                self.dfs(rooms, m, n, next_i, next_j)