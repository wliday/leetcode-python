class Solution(object):
    def searchInsert(self, nums, target):
        if not nums or target < nums[0]:
            return 0

        if target > nums[-1]:
            return len(nums)

        start, end = 0, len(nums) - 1
        while start <= end:
            mid = start + (end - start) / 2

            if target < nums[mid]:
                mid = end - 1
            elif target > nums[mid]:
                mid = start + 1
            else:
                return mid
        return start