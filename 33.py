class Solution(object):
    def search(self, nums, target):
        if not nums: return -1

        start, end = 0, len(nums) - 1
        while start <= end:
            mid = start + ((end - start) >> 1)
            if nums[mid] == target:
                return mid

            if nums[start] <= nums[mid]:
                if nums[start] <= target and target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            elif nums[mid] <= nums[end]:
                if nums[mid] < target and target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1

        return -1
