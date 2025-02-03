class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        vel = 0
        longest = 1
        cur = 1
        for i in range(1, len(nums)):
            cur_vel = nums[i] - nums[i - 1]
            if cur_vel * vel >= 0 and cur_vel != 0:
                cur += 1
            else:
                longest = max(longest, cur)
                cur = 1 if cur_vel == 0 else 2
            vel = cur_vel
        longest = max(longest, cur)
        return longest
