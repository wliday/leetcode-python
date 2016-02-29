class Solution(object):
	def reverseWords(self, s):
		if not s: return None
		self.reverse(s, 0, len(s) - 1)

		r = 0
		while r < len(s):
			l = r
			while r < len(s) and s[r] != ' ':
				r += 1
			self.reverse(s, l, r  - 1)
			r += 1
		print s

	def reverse(self, s, l, r):
		while l < r:
			s[l], s[r] = s[r], s[l]
			l += 1
			r -= 1