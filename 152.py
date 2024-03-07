class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_prod = 1
        cur_neg_prod = -float("infinity")
        track_max = -float("infinity")
        has_zero = False
        for i in range(len(nums)):
            if nums[i] == 0:
                has_zero = True
                cur_prod = 1
                cur_neg_prod = -float("infinity")
                continue
            cur_prod *= nums[i]
            track_max = max(track_max, cur_prod)
            if nums[i] < 0 and cur_prod < 0:
                cur_neg_prod = max(cur_prod, cur_neg_prod)
                continue
            if cur_prod < 0:
                track_max = max(track_max, cur_prod // cur_neg_prod)
        if track_max < 0:
            return 0 if has_zero else track_max
        return track_max
