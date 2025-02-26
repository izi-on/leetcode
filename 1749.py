class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        def passs(nums):
            cur_sum = 0
            tail = 0
            track_max = 0
            for i in range(0, len(nums)):
                cur_sum += nums[i]
                if cur_sum < 0:
                    tail = i + 1
                    cur_sum = 0
                else:
                    track_max = max(cur_sum, track_max)
            return track_max

        return max(passs(nums), passs([-num for num in nums]))
