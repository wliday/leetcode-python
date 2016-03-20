class Solution:

    def subarraySumClosest(self, nums):
        if not nums: return []
        if len(nums) == 1: return [0, 0]
        
        sums = [(0, 0)]
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            sums.append((sum, i + 1))
        
        sums.sort()

        min_diff = float("inf")
        result = [0, 0]
        for i in range(1, len(sums)):
            sum_diff = abs(sums[i][0] - sums[i - 1][0]) 
            if sum_diff < min_diff:
                min_diff = sum_diff
                result[0], result[1] = min(sums[i - 1][1], sums[i][1]), max(sums[i - 1][1], sums[i][1]) - 1
        
        return result