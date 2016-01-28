class Solution(object):
    def searchInsert(self, nums, target):
        if not nums or target < nums[0]:
            return 0

        if target > nums[-1]:
            return len(nums)

        return self.binarySearch(nums, 0, len(nums) - 1, target)

    def binarySearch(self, nums, start, end, target):
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = start + (end - start) / 2

            if target == nums[mid]:
                return mid
            if target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1

        return start