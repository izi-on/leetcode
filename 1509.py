import heapq


class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 4:
            return 0
        nums = sorted(nums)
        ans = float("infinity")
        for i in range(3):
            ans = min(ans, nums[-1 - (3 - i)] - nums[i])
        return ans
