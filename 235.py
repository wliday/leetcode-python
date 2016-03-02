class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if not root or not p or not q: return None

        while (p.val - root.val) * (q.val - root.val) > 0:
            root = root.right if root.val < p.val else root.left

        return root