class Solution(object):
    def countPrimes(self, n):
        primes = [False, False] + [True] * (n - 2)
        for i in range(2, int(n ** 0.5 + 1)):
            if not primes[i]: continue

            for j in range(i * i, n, i):
                primes[j] = False

        return sum(primes)