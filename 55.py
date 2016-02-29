class Solution(object):
    def canJump(self, nums):
        if not nums: return False
        if len(nums) == 1: return True

        end = len(nums) - 1
        for start in range(len(nums) - 2, -1, -1):
            if nums[start] >= end - start:
                end = start

        return end == 0