class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums = sorted(nums, reverse=True)
        count = 0
        cur_lvl = nums[0]
        for i in range(len(nums)):
            count += bool(cur_lvl - nums[i]) * i
            cur_lvl = nums[i]
        return count
