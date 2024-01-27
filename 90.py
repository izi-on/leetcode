class Solution:
    def __init__(self):
        self.answer = set()

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, cur):
            if not nums:
                self.answer.add(tuple(cur))
                return
            dfs(nums[1:], cur)
            cur.append(nums[0])
            dfs(nums[1:], cur)
            cur.pop()

        nums = sorted(nums)
        dfs(nums, [])
        return list(map(lambda x: list(x), self.answer))
