class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total = 0

        def helper(cur_sum, idx):
            nonlocal total
            if idx == len(nums):
                total += cur_sum
                return
            helper(cur_sum, idx + 1)
            helper(cur_sum ^ nums[idx], idx + 1)

        helper(0, 0)
        return total
