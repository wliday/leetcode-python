class Solution(object):
    
    min_cnt = float("inf")
    
    def coinChange(self, coins, amount):
        if not coins or not amount: return 0

        coins.sort()
        self.dfs(coins, len(coins) - 1, amount, 0)
        return self.min_cnt if self.min_cnt < float("inf") else -1


    def dfs(self, coins, index, amount, cnt):
        if index < 0: return

        n = amount / coins[index]
        for i in range(n, -1, -1):
            remain = amount - coins[index] * i
            new_cnt = cnt + i
            if new_cnt > self.min_cnt:
                break
            
            if remain > 0:
                self.dfs(coins, index - 1, remain, new_cnt)
            elif remain == 0:
                self.min_cnt = new_cnt
            else:
                break