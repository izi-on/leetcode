class Solution:
    def __init__(self):
        self.answer = []
        self.cur_permutation = []

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(i, candidates, target):
            print(self.cur_permutation, candidates)
            if i >= len(candidates):
                return
            if target < 0:
                return
            if target == 0:
                self.answer.append(self.cur_permutation.copy())
                return
            dfs(i + 1, candidates, target)
            self.cur_permutation.append(candidates[i])
            dfs(i, candidates, target - candidates[i])
            self.cur_permutation.pop()

        dfs(0, candidates, target)
        return self.answer
