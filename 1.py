class Solution(object):
	def twoSum(self, nums, target):
		if not nums: return []
		hash_dict = {}

		for i in range(len(nums)):
			if target - nums[i] in hash_dict:
				return [hash_dict[target - nums[i]], i + 1]
				
			hash_dict[nums[i]] = i + 1

		return [0, 0]