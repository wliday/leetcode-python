class Solution(object):
	def findKthLargest(self, nums, k):
		return self.findKthSmallest(nums, len(nums) - k + 1)

	def findKthSmallest(self, nums, k):
		if not nums: return None

		pos = self.partition(nums, 0, len(nums) - 1)
		if k > pos + 1:
			return self.findKthSmallest(nums[pos + 1:],  k - pos - 1)
		elif k < pos + 1:
			return self.findKthSmallest(nums[:pos], k)
		else:
			return nums[pos]

	def partition(self, nums, left, right):
		pivot = nums[left]
		while left < right:
			while left < right and nums[right] >= pivot:
				right -= 1
			nums[left], nums[right] = nums[right], nums[left]
			
			while left < right and nums[left] <= pivot:
				left += 1
			nums[left], nums[right] = nums[right], nums[left]
		
		return left