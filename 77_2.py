class Solution(object):
    def combine(self, n, k):
        result = []
        self.dfs(n, k, 1, [], result)
        return result

    def dfs(self, n, k, index, path, result):
        if len(path) > k: return
        if len(path) == k: 
            result.append(path)
            return
        if len(path) < k:
            for i in range(index, n + 1):
                    self.dfs(n, k, i + 1, path + [i], result)

print Solution().combine(4, 4)
