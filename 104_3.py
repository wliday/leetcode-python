class Solution(object):
	def maxDepth(self, root):
		if not root: return 0
		
		from collections import deque

		queue = deque([(root, 1)])
		while queue:
			node, level = queue.popleft()

			if node.left:
				queue.append([node.left, level + 1])
			if node.right:
				queue.append([node.right, level + 1])

		return level