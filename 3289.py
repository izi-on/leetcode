class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        def run_tortoise_and_hare(start):
            f, s = nums[nums[start]], nums[start]
            while f != s:
                f = nums[nums[f]]
                s = nums[s]
            f = start
            while f != s:
                f = nums[f]
                s = nums[s]
            return s

        bl, l = len(nums) - 2, len(nums) - 1
        dup1 = run_tortoise_and_hare(l)
        dup2 = run_tortoise_and_hare(bl)
        if dup1 != dup2:
            return [dup1, dup2]
        nums[dup1] = l
        dup2 = run_tortoise_and_hare(bl)
        return [dup1, dup2]
