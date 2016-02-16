class Solution(object):
    def subsets(self, nums):
        nums.sort()
        res = [[] for _ in range(1 << len(nums))]

        for i in range(len(nums)):
            for j in range(1 << len(nums)):
                if (j >> i) & 1:
                    res[j].append(nums[i])

        return res