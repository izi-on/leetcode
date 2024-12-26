from collections import defaultdict


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[nums[0]] += 1
        dp[-nums[0]] += 1
        for num in nums[1:]:
            temp_dp = defaultdict(int)
            for key in dp.keys():
                temp_dp[key + num] += dp[key]
                temp_dp[key - num] += dp[key]
            dp = temp_dp
        return dp[target]
