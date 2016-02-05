class Solution(object):
    def minDistance(self, word1, word2):

        if len(word1) == 0 or len(word2) == 0:
            return len(word1) + len(word2)

        m, n = len(word1) + 1, len(word2) + 1

        dp = [([0] * n) for _ in range(m)]

        for i in range(m):
            dp[i][0] = i

        for j in range(n):
            dp[0][j] = j

        for i in range(1, m):
            for j in range(1, n):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

        return dp[m - 1][n - 1]
