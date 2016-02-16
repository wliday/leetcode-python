class Solution(object):
    def subsets(self, nums):
        if not nums: return []
        result = [[]]
        nums.sort()
        for num in nums:
            result += [item + [num] for item in result]

        return result
