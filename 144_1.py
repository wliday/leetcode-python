class Solution(object):
    def preorderTraversal(self, root):
        if not root: return []
        stack, result = [], []
        while stack or root:
            if root:
                stack.append(root)
                result.append(root.val)# Add before going to children
                root = root.left
            else:
                node = stack.pop()
                root = node.right
        return result