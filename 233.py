class Solution(object):
    def countDigitOne(self, n):
        ones, m = 0, 1
        while m <= n:
            a = n / m
            b = n % m
            ones += (a + 8) / 10 * m + (a % 10 == 1) * (b + 1)
            m *= 10
        return ones
