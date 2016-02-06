class Solution(object):
	def wordPattern(self, pattern, str):

		words = str.split()
		if len(pattern) != len(words):
			return False

		hash_dict = {}
		for i in range(len(pattern)):
			if pattern[i] not in hash_dict:
				if words[i] in hash_dict.values():
					return False
				hash_dict[pattern[i]] = words[i]
			else:
				if hash_dict[pattern[i]] != words[i]:
					return False

		return True

