class Solution(object):
    def combinationSum(self, candidates, target):
        result = []
        self.dfs(sorted(candidates), target, 0, [], result)
        return result

    def dfs(self, candidates, target, index, path, result):
        if target == 0:
            result.append(path)
            return
            
        for i in range(index, len(candidates)):
            if target - candidates[i] < 0: 
                break
            self.dfs(candidates, target - candidates[i], i, path + [candidates[i]], result)