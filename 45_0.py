# DP, but TLE
class Solution(object):
    def jump(self, nums):
        if not nums or len(nums) == 1: return 0

        steps = [0] + [float("inf")] * (len(nums) - 1)
        for i in range(len(nums) - 1):
            if not nums[i]: continue
            for j in range(1, nums[i] + 1):
                if i + j > len(nums) - 1: break

                steps[i + j] = min(steps[i + j], steps[i] + 1)
                if i + j == len(nums) - 1: return steps[i + j]

        return steps[-1]