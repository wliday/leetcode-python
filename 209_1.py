class Solution(object):
    def minSubArrayLen(self, s, nums):
    	if not nums: return 0
    	slow, fast, sum, min_len = 0, 0, 0, len(nums) + 1

    	while fast < len(nums):
    		sum += nums[fast]
    		fast += 1

    		while sum >= s:
    			min_len = min(fast - slow, min_len)
    			sum -= nums[slow]
    			slow += 1

    	return 0 if min_len == len(nums) + 1 else min_len