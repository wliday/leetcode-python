class Solution(object):
	def findKthLargest(self, nums, k):
		if not nums or len(nums) < k: 
			return None

		nums.sort()
		return nums[-k]