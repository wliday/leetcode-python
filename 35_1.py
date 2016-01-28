class Solution(object):
    def searchInsert(self, nums, target):
        if not nums or target < nums[0]:
            return 0

        if target > nums[-1]:
            return len(nums)

        return self.binarySearch(nums, 0, len(nums) - 1, target)

    def binarySearch(self, nums, start, end, target):
        if start > end:
            return start
        mid = start + (end - start) / 2
        if target < nums[mid]:
            return self.binarySearch(nums, start, mid - 1, target)
        elif target > nums[mid]:
            return self.binarySearch(nums, mid + 1, end, target)
        else:
            return mid