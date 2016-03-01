class Solution:
    def numDecodings(self, s):
        if not s : return 0
        if s[0] == '0': return 0
        if len(s) == 1 and s[0] != '0': return 1

        dp = [0] * (len(s) + 1)
        dp[len(s)] = 1
        if s[-1] != '0': dp[len(s)-1] = 1

        for i in range(len(s) - 2, -1, -1):
            if s[i] == '0': continue
            if "10" <= s[i : i + 2] <= "26":
                dp[i] = dp[i + 1] + dp[i + 2]
            else:
                dp[i] = dp[i + 1]

        return dp[0]