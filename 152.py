from types import TracebackType


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_prod = 1
        cur_neg_subarr = 1
        track_max = -float("infinity")
        has_zero = False
        for i in range(len(nums)):
            if nums[i] == 0:
                has_zero = True
                cur_prod = 1
                cur_neg_subarr = 1
                track_max = max(track_max, 0)
                continue
            cur_prod *= nums[i]
            track_max = max(track_max, cur_prod)
            if cur_prod < 0 and cur_neg_subarr == 1:
                cur_neg_subarr = cur_prod
                continue
            if cur_prod < 0:
                track_max = max(track_max, cur_prod // cur_neg_subarr)
        return track_max
