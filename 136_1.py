class Solution(object):
    def singleNumber(self, nums):
        if not nums: return None
        result = 0
        for num in nums:
            result ^= num
            print result
        return result