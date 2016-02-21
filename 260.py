class Solution(object):
	def singleNumber(self, nums):
		if not nums: return []
		if len(nums) == 2: return nums

		diff = reduce(lambda x, y: x^y, nums)
		diff &= -diff

		one, two = 0, 0
		for num in nums:
			if num & diff:
				one ^= num
			else:
				two ^= num
		return [one, two]