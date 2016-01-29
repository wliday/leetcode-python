class Solution(object):
	def maxDepth(self, node):
	    if not node: return 0

	    l_depth = self.maxDepth(node.left)
	    r_depth = self.maxDepth(node.right)

	    return max(l_depth, r_depth) + 1