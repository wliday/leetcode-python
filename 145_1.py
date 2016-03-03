class Solution(object):
    def postorderTraversal(self, root):
     	if not root: return []
    	stack, result = [], []
    	while stack or root:
    		if root:
    			stack.append(root)
    			result.insert(0, root.val)
    			root = root.right
    		else:
    			node = stack.pop()
    			root = node.left
    	return result