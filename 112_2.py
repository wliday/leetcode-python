class Solution(object):
    def hasPathSum(self, root, sum):
    	if not root: return False

    	if not root.left and not root.right and sum == root.val:
    		return True

    	if root.left:
    		root.left.val += root.val
    	if root.right:
    		root.right.val += root.val

    	return self.hasPathPath(root.left, sum) or self.hasPathSum(root.right, sum)