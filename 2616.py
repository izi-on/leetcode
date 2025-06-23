class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        s_n = sorted(nums)
        return s_n[2 * p + 1] - s_n[2 * p]
