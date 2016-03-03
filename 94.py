class Solution(object):
    def inorderTraversal(self, root):
        if not root: return []

        stack, result = [], []
        while stack or root:
        	if root:
        		stack.append(root)
        		root = root.left
        	else:
        		node = stack.pop()
        		result.append(node.val)
        		root = node.right
        return result