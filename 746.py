class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        min_cost_dp = [0 for _ in range(n + 1)]
        for i in range(2, n + 1):
            min_cost_dp[i] = min(
                min_cost_dp[i - 2] + cost[i - 1], min_cost_dp[i - 2] + cost[i - 2]
            )
        return min_cost_dp[n]
