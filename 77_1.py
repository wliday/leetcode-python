class Solution(object):
    def combine(self, n, k):
        if k == 1:
            return [[x] for x in range(1, n + 1)]
        if k == n:
            return [[x for x in range(1, n + 1)]]

        result = []
        result.extend(self.combine(n - 1, k))

        part = self.combine(n - 1, k - 1)
        part[:] = [x + [n] for x in part]
        result.extend(part)

        return result

print Solution().combine(4, 2)

