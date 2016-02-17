class Solution(object):
    def combinationSum3(self, k, n):
        result = []
        self.dfs(1, k, n, [], result)
        return result

    def dfs(self, index, k, n, path, result):
        if k == 0 and n == 0:
            result.append(path)
            return
        if n < 0 or k <= 0:
            return

        for i in range(index, 10):
            if i <= n:
                self.dfs(i + 1, k - 1, n - i, path + [i], result)