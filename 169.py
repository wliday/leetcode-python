class Solution(object):
    def majorityElement(self, nums):
    	major, count = 0, 0

    	for num in nums:
    		if not count:
    			major, count = num , 1
    		else:
    			count += 1 if major == num else 0

    	return major