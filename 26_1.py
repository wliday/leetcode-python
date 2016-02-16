class Solution(object):
    def removeDuplicates(self, nums):
        nums[:] = [nums[x]
                   for x in range(len(nums))
                        if nums[x] != nums[x - 1] or x == 0
                   ]
        return len(nums)