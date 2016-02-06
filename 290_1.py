class Solution(object):
	def wordPattern(self, pattern, str):
		hash_pattern, hash_str = {}, {}

		list1, list2 = [], []

		index = 0
		for c in pattern:
			if c not in hash_pattern:
				hash_pattern[c] = index
				list1.append(index)
				index += 1
			else:
				list1.append(hash_pattern[c])

		index = 0
		str_list = str.split()
		for s in str_list:
			if s not in hash_str:
				hash_str[s] = index
				list2.append(index)
				index += 1
			else:
				list2.append(hash_str[s])

		return list1 == list2

print Solution().wordPattern("abba", "dog cat cat dog")

