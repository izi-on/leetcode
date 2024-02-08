class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        track_max = -float("infinity")
        cur_sub = 0
        for num in nums:
            cur_sub += num
            track_max = max(track_max, cur_sub)
            if cur_sub < 0:
                cur_sub = 0
        return track_max
