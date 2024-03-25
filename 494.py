from collections import defaultdict


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[(-1, 0):1]

        def dfs(n_idx, target):
            if n_idx == -1:
                return 0
            if (n_idx, target) in dp:
                return dp[(n_idx, target)]
            ways = dfs(n_idx - 1, target + nums[n_idx]) + dfs(
                n_idx - 1, target - nums[n_idx]
            )
            dp[(n_idx, target)] = ways
            return ways

        return dfs(len(nums), target)
