class Solution(object):
    def combinationSum2(self, candidates, target):
        result = []
        self.dfs(target, 0, sorted(candidates), [], result)
        
        return result

    def dfs(self, target, index, candidates, path, result):
        if target == 0:
            result.append(path)
            return
        if target < 0:
            return 

        for i in range(index, len(candidates)):
            if i > index and candidates[i] == candidates[i - 1]:
                continue
            if candidates[i] <= target:
                self.dfs(target - candidates[i], i + 1, candidates, path + [candidates[i]], result)
