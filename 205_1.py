class Solution(object):	
	def isIsomorphic(self, s, t):
		if not s and not t:
			return True

		hash_s, hash_t = {}, {}
		ls, lt = [], []
		c1, c2 = 0, 0
		for i in range(len(s)):
			if s[i] not in hash_s:
				hash_s[s[i]] = c1
				ls.append(c1)
				c1 += 1
			else:
				ls.append(hash_s[s[i]])
			
			if t[i] not in hash_t:
				hash_t[t[i]] = c2
				lt.append(c2)
				c2 += 1
			else:
				lt.append(hash_t[t[i]])
		return ls[:] == lt[:]
