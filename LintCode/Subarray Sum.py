class Solution:
    def subarraySum(self, nums):
        sums = [(0, 0)]
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            sums.append((sum, i + 1))
        
        sums.sort()

        for i in range(1, len(sums)):
            if sums[i][0] == sums[i - 1][0]:
                return [sums[i - 1][1], sums[i][1] - 1]
        return [-1, -1]