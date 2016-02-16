class Solution(object):
    def fourSum(self, nums, target):
        if len(nums) < 4: return []

        nums.sort()

        result = []
        for i in range(len(nums) - 3):
            if nums[i] * 4 > target:
                break
            if i != 0 and nums[i] == nums[i - 1]:
                continue

            target3 = target - nums[i]
            for j in range(i + 1, len(nums) - 2):
                if nums[j] * 3 > target3:
                    break
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                target2 = target3 - nums[j]
                start, end = j + 1, len(nums) - 1
                while start < end and nums[start] <= (target2 >> 1) and nums[end] >= (target2 >> 1):
                    if nums[start] + nums[end] == target2:
                        result.append([nums[i], nums[j], nums[start], nums[end]])
                        while start < end and nums[start] == nums[start + 1]: start += 1
                        while start < end and nums[end] == nums[end - 1]: end -= 1
                    if nums[start] + nums[end] < target2:
                        while start < end and nums[start] == nums[start + 1]: start += 1
                        start += 1
                    else:
                        while start < end and nums[end] == nums[end - 1]: end -= 1
                        end -= 1


        return result