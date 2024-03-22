class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0 for _ in coins] for _ in range(amount + 1)]
        dp[0] = [1 for _ in coins]
        for i in range(1, amount + 1):
            for j in range(len(coins)):
                new_coin = coins[j]
                to_add_vertical = dp[i - new_coin][j] if i - coins[j] >= 0 else 0
                to_add_horizontal = dp[i][j - 1] if j - 1 >= 0 else 0
                dp[i][j] = to_add_vertical + to_add_horizontal
        return dp[amount][len(coins) - 1]
