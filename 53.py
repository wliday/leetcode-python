class Solution(object):
    def maxSubArray(self, nums):
        if not nums: return 0

        dp = [0] * len(nums)
        res = nums[0]

        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], dp[i - 1] + nums[i])
            res = max(res, dp[i])

        return res