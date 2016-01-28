class Solution(object):
    def searchRange(self, nums, target):
        if not nums: return 0
        if target < nums[0] or target > nums[-1]: return [-1, -1]

        start = self.binarySearch(nums, 0, len(nums) - 1, target - 0.1)

        if nums[start] != target:
            return [-1, -1]

        end = self.binarySearch(nums, 0, len(nums) - 1, target + 0.1)

        return [start, end - 1]

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