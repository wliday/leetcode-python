
class Solution(object):
	def levelOrder(self, root):
		result, level = [], [root]
		while level:
			result.append([node.val for node in level])
			level = [kid for node in level for kid in (node.left, node.right) if kid]
		return result


