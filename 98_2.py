class Solution(object):
	def isValidBST(self, root):
		max = float("inf")
		min = -float("inf")
		return self.isValid(min, root, max)

	def isValid(self, left, node, right):
		if not node: return True
		if left >= node.val or node.val >= right: return False
		
		return self.isValid(left, node.left, node.val) and self.isValid(node.val, node.right, right)
