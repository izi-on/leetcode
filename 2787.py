class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD = 10**9 + 7
        dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(n + 1):
            for j in range(1, n + 1):
                dp[i][j] = dp[i][j - 1]  # dont include current number
                if j**x <= i:  # include current number
                    # print("dp", i, j, "looking at dp", i - j**x, j-1, "cur val: ", dp[i][j])
                    dp[i][j] = (dp[i][j] + dp[i - j**x][j - 1]) % MOD
                    # print("after", dp[i][j])
        # print(dp)
        return dp[n][n]
