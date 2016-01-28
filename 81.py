class Solution(object):
    def search(self, nums, target):
        if not nums: return False
        start, end = 0, len(nums) - 1

        while start <= end:
            mid = (end - start) / 2 + start
            if nums[mid] == target: return True

            if nums[start] < nums[mid]:  # left is sorted
                if nums[start] <= target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            elif nums[mid] < nums[end]: # right is sorted
                if nums[mid] < target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
            else: # can't determine in which side
                if nums[start] == target:
                    return True
                else:
                    start += 1

        return False