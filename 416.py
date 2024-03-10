from collections import defaultdict
from collections import deque


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 == 1:
            return False
        target = total_sum // 2
        possible_sum = set()
        possible_sum.add(0)
        for i in range(len(nums)):
            for s in list(possible_sum):
                possible_sum.add(s + nums[i])
            if target in possible_sum:
                return True
        return False
