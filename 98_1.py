class Solution(object):
    def isValidBST(self, root):
        inorder_list = []
        self.inorder(root, inorder_list)

        for i in range(1, len(inorder_list)):
            if inorder_list[i - 1] >= inorder_list[i]:
                return False
        return True

    def inorder(self, node, output):
        if not node: return
        self.inorder(node.left, output)
        output.append(node.val)
        self.inorder(node.right, output)