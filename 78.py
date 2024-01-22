class Solution:
    def __init__(self):
        self.ans = []

    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(idx, cur_subset):
            if idx == len(nums):
                self.ans += cur_subset
                return
            dfs(idx + 1, cur_subset)
            cur_subset.append(nums[idx])
            dfs(idx + 1, cur_subset)
            cur_subset.pop()

        dfs(0, [])
        return self.ans
