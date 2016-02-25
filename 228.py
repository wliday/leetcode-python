class Solution(object):
    def summaryRanges(self, nums):
        if not nums: return []
        
        start, end = 0, 0
        result = []
        nums = nums + [nums[-1] + 2]
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:
                end = i - 1
                if start == end: 
                    result.append("" + str(nums[start]))
                else:
                    result.append("" + str(nums[start]) + "->" + str(nums[end]))
                start, end = i, i
        return result
                