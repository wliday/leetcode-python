class Solution(object):
	def threeSum(self, nums):
		if len(nums) < 3: return []
		nums.sort()

		result = []
		for i in range(len(nums)):
			target = 0 - nums[i]
			start, end = i + 1, len(nums) - 1
			while start < end:
				if nums[start] + nums[end] == target:
					result.append([nums[i], nums[start], nums[end]])

				if nums[start] + nums[end] < target:
					start += 1
				else:
					end -= 1

		result.sort()

		return [result[i] for i in range(0, len(result)) if result[i] != result[i - 1] or i == 0]