class Solution(object):
    def minSubArrayLen(self, s, nums):
    	if not nums: return 0
    	
    	sums = [0 for i in range(len(nums) + 1)]
    	for i in range(1, len(nums) + 1):
    		sums[i] = sums[i - 1] + nums[i - 1]
    	print sums
    	
    	min_len = float("inf")
    	for i in range(len(nums)):
    		end = self.binarySearch(i + 1, len(nums), sums[i] + s, sums)

    		if end >= len(sums): break
    		min_len = min(min_len, end - i)

    	return 0 if min_len == float("inf") else min_len

    def binarySearch(self, start, end, target, sums):
    	while start <= end:
    		mid = start + (end - start) / 2
    		if target < sums[mid]:
    			end = mid - 1;
    		elif target > sums[mid]:
    			start = mid + 1
    		else:
    			return mid

    	return start