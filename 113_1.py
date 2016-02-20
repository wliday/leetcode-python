class Solution(object):
    def pathSum(self, root, sum):
        result = []
        self.dfs(root, sum, [], result)

        return result

    def dfs(self, root, sum, path, result):
        if not root: return

        if not root.left and not root.right and sum == root.val:
            path.append(root.val)
            result.append(path)

        self.dfs(root.left, sum - root.val, path + [root.val], result)
        self.dfs(root.right, sum - root.val, path + [root.val], result)