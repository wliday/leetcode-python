class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums: return 0
        if target < nums[0] or target > nums[-1]: return [-1, -1]

        start = self.binarySearch(nums, 0, len(nums), target)

        if nums[start] != target:
            return [-1, -1]

        end = self.binarySearch(nums, 0, len(nums), target + 1) - 1

        return [start, end]

    def binarySearch(self, nums, start, end, target):
        if start >= end:
            return start

        mid = start + ((end - start) >> 1)

        if nums[mid] < target:
            return self.binarySearch(nums, mid + 1, end, target)
        else:
            return self.binarySearch(nums, start, mid, target)

