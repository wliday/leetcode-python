class Solution(object):
    def jump(self, nums):
        if not nums or len(nums) == 1: return 0
        start, end, step = 0, 0, 0
        while end < len(nums) - 1:
            step += 1

            max_end = end + 1
            for i in range(start, end + 1):
                if nums[i] + i >= len(nums) - 1:
                    return step
                max_end = max(max_end, nums[i] + i)
            start, end = start + 1, max_end

        return step