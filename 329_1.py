class Solution(object):
   
    def longestIncreasingPath(self, matrix):
        if not len(matrix) or not len(matrix[0]): return 0
        m, n = len(matrix), len(matrix[0])
        cache = [[0] * n for _ in range(m)]

        dires = ((0, 1), (0, -1), (-1, 0), (1, 0))

        def dfs(i, j):
            if cache[i][j] > 0: return cache[i][j]

            max_length = 1
            for dire in dires:
                next_i = i + dire[0]
                next_j = j + dire[1]
                if next_i < 0 or next_i >= m or next_j < 0 or next_j >= n or matrix[next_i][next_j] <= matrix[i][j]:
                    continue
                length = 1 + dfs(next_i, next_j)
                max_length = max(max_length, length)

            cache[i][j] = max_length
            return max_length

        return max(dfs(i, j) for i in range(m) for j in range(n))