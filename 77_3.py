class Solution(object):
    def combine(self, n, k):
        result = []
        self.dfs(1, n, k, [], result)
        return result

    def dfs(self, index, n, k, path, result):
        if k == 0:
            result.append(path)
            return 
        for i in range(index, n + 1):
            self.dfs(i + 1, n, k - 1, path + [i], result)
