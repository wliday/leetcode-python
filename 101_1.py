class Solution(object):
    def isSymmetric(self, root):
        if not root: return True
        return self.isSymmetricHelp(root.left, root.right)

    def isSymmetricHelp(self, lnode, rnode):

        if not lnode or not rnode:
            return lnode == rnode

        return lnode.val == rnode.val and self.isSymmetricHelp(lnode.left, rnode.right) and self.isSymmetricHelp(lnode.right, rnode.left)