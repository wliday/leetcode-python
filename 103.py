class Solution(object):
    def zigzagLevelOrder(self, root):
    	if not root: return None

        ans, level = [], [root]
        while level:
            if len(ans) % 2 == 0:
                ans.append([node.val for node in level])
            else:
                ans.append(list(reversed([node.val for node in level])))
            level = [leaf for node in level for leaf in (node.left, node.right) if leaf]
        return ans