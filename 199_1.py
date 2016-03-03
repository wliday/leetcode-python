class Solution(object):
    def rightSideView(self, root):
        if not root: return []
        
        result, level = [], [root]
        while level:
            result.append(level[-1].val)
            level = [kid for node in level for kid in (node.left, node.right) if kid]
        return result