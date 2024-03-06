class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("infinity") for _ in range(amount + 1)]
        dp[0] = 0
        for i in range(amount + 1):
            for coin in coins:
                if i - coin < 0:
                    continue
                dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[amount] if dp[amount] != float("infinity") else -1
