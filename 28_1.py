class Solution(object):
	def strStr(self, haystack, needle):
		if haystack is None or needle is None: 
			return -1

		haystack = list(haystack)
		needle = list(needle)

		for i in range(len(haystack) - len(needle) + 1):
			j = 0
			while j < len(needle):
				if haystack[i + j] != needle[j]:
					break
				else:
					j += 1
			
			if j == len(needle):
				return i

		return -1
