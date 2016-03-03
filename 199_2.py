class Solution(object):
    def rightSideView(self, root):
        if not root: return []
        return self.dfs(root, 0, [])
    
    def dfs(self, root, level, result):
        if not root: return result
        if len(result) == level: result.append(root.val)
        self.dfs(root.right, level + 1, result)
        self.dfs(root.left, level + 1, result)
        return result