class Solution(object):
    def pathSum(self, root, sum):
        if not root: return []
        result = []

        from collections import deque
        queue = deque([(root, 0, [])])
        while queue:
        	curr, val, ls = queue.popleft()
        	if not curr.left and not curr.right and val == sum:
        		result.append(ls + [curr.val])

        	if curr.left:
        		queue.append((curr.left, val - curr.val, ls + [curr.val]))
        	if curr.right:
        		queue.append((curr.right, val - curr.val, ls + [curr.val]))

        return result
