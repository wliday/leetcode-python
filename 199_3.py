class Solution(object):
    def rightSideView(self, root):
        if not root: return []
       
        def dfs(root, level):
            if not root: return 
            if len(result) == level: result.append(root.val)
            dfs(root.right, level + 1)
            dfs(root.left, level + 1)
        
        result = []
        dfs(root, 0)
        return result