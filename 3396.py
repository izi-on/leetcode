import math


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums_set = set()
        is_at = -1
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] in nums_set:
                is_at = i
                break
            nums_set.add(nums[i])
        return math.ceil((is_at + 1) / 3)
