class Solution(object):
	def isSymmetric(self, root):
		if not root: return True

		stack = [[root.left, root.right]]
		while stack:
			lnode, rnode = stack.pop()
			
			if (not lnode) and (not rnode):
				continue

			if (not lnode) or (not rnode):
				return False

			if lnode and rnode and lnode.val != rnode.val:
				return False

			stack.extend([[lnode.left, rnode.right], [lnode.right, rnode.left]])

		return True



