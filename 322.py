class Solution(object):
    def coinChange(self, coins, amount):
        dp = [amount + 1 for _ in range(amount + 1)]

        dp[0] = 0
           for i in range(amount + 1):
               if i - coin < 0: continue
               dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[amount] if dp[amount] <= amount else -1