class Solution(object):
	def isAnagram(self, s, t):
		hash_dict = {}

		for c in s:
			if c in hash_dict:
				hash_dict[c] += 1
			else:
				hash_dict[c] = 1
		for c in t:
			if c in hash_dict:
				hash_dict[c] -= 1
			else:
				return False
		for v in hash_dict.values():
			if v != 0:
				return False

		return True




