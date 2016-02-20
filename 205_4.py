class Solution(object):	
	def isIsomorphic(self, s, t):
		return [s.find(c) for c in s] == [t.find(c) for c in t]