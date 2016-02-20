class Solution(object):
    def pathSum(self, root, sum):
        if not root: return []
        result = []
        stack = [(root, sum, [])]
        while stack:
        	curr, val, ls = stack.pop()
        	if not curr.left and not curr.right and val == curr.val:
        		result.append(ls + [curr.val])

        	if curr.left:
        		stack.append((curr.left, val - curr.val, ls + [curr.val]))
        	if curr.right:
        		stack.append((curr.right, val - curr.val, ls + [curr.val]))

        return result