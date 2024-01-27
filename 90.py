class Solution:
    def __init__(self):
        self.answer = []

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def dfs(idx, nums, cur):
            if idx == len(nums):
                self.answer.append(cur)
                return
            # chose to include current number
            cur.append(nums[idx])
            dfs(idx + 1, nums, cur)
            cur.pop()
            # chose not to include current number
            while idx != len(nums) - 1 and nums[idx] == nums[idx + 1]:
                idx += 1
            dfs(idx + 1, nums, cur)

        nums = sorted(nums)
        dfs(0, nums, [])
        return list(map(lambda x: list(x), self.answer))
