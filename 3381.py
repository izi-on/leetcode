class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        # i - (j-1) MOD k = 0
        # i + 1 MOD k = j MOD k
        tmax = -float("inf")
        prefix_sum = 0
        track_smallest = [float("inf")] * (k + 1)
        track_smallest[0] = 0
        for i in range(len(nums)):
            prefix_sum += nums[i]
            if i + 1 >= k:
                tmax = max(tmax, prefix_sum - track_smallest[(i + 1) % k])
            track_smallest[(i + 1) % k] = min(track_smallest[(i + 1) % k], prefix_sum)
        return tmax
