class Solution(object):
    def maxDepth(self, root):
        res = 0
        stack = [(root, 0)]
        while stack:
            node, level = stack.pop()
            if not node:
                res = max(res, level)
            else:
                stack.append((node.right, level + 1))
                stack.append((node.left, level + 1))
        return res
