class Solution(object):
	def threeSum(self, nums):
		if len(nums) < 3: return []
		nums.sort()

		result = []
		for i in range(len(nums) - 2):
			if i == 0 or nums[i] != nums[i - 1]:
				target = 0 - nums[i]
				start, end = i + 1, len(nums) - 1
				while start < end:
					if nums[start] + nums[end] == target:
						result.append([nums[i], nums[start], nums[end]])
						while start < end and nums[start] == nums[start + 1]: start += 1
						while start < end and nums[end] == nums[end - 1]: end -=1

					if nums[start] + nums[end] < target:
						while start < end and nums[start] == nums[start + 1]: start += 1
						start += 1
					else:
						while start < end and nums[end] == nums[end - 1]: end -= 1
						end -= 1

		return result