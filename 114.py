
class Solution(object):
    def flatten(self, root):
        if not root: return None

        preorder_list = self.preorder_traverse(root, [])

        for i in range(0, len(preorder_list) - 1):
            preorder_list[i].left, preorder_list[i].right = None, preorder_list[i + 1]
        preorder_list[-1].left = preorder_list[-1].right = None

        return 

    def preorder_traverse(self, node, preorder_list):
        preorder_list.append(node)
        if node.left:
            self.preorder_traverse(node.left, preorder_list)
        if node.right:
            self.preorder_traverse(node.right, preorder_list)
        return preorder_list