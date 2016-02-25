class Solution(object):
    def isPowerOfTwo(self, n):
        for i in range(32):
            if 1 << i == n:
                return True
        return False