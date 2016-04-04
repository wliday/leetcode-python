class Solution(object):
    def combinationSum2(self, candidates, target):
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
            if i > index and candidates[i] == candidates[i - 1]:
                continue
            self.dfs(candidates, target - candidates[i], i + 1, path + [candidates[i]], result)