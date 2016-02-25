class Solution(object):
    def isPowerOfThree(self, n):
        if n <= 0: return False
        
        import math
        maxPower = pow(3, math.floor(math.log(pow(2, 31) - 1, 3)))

        return True if maxPower % n == 0 else False