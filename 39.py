class Solution:
    def __init__(self):
        self.answer = []
        self.cur_permutation = []

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(candidates, target):
            print(self.cur_permutation, candidates)
            if not candidates:
                return
            if target < 0:
                return
            if target == 0:
                self.answer.append(self.cur_permutation.copy())
                return
            self.combinationSum(candidates[1:], target)
            self.cur_permutation.append(candidates[0])
            self.combinationSum(candidates, target - candidates[0])
            self.cur_permutation.pop()

        dfs(candidates, target)
        return self.answer
