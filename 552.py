class Solution:
    def checkRecord(self, n: int) -> int:
        to_mod = 10**9 + 7
        dp = [[[0 for _ in range(3)] for _ in range(2)] for _ in range(n + 1)]
        dp[1][0][0] = 1
        dp[1][1][0] = 1
        dp[1][0][1] = 1
        for i in range(1, n):
            for j in range(2):
                for k in range(3):
                    # CASE 1: pick P
                    dp[i + 1][j][0] = (dp[i + 1][j][0] + dp[i][j][k]) % to_mod

                    # CASE 2: pick A
                    if j < 1:
                        dp[i + 1][j + 1][0] = (
                            dp[i + 1][j + 1][0] + dp[i][j][k]
                        ) % to_mod

                    # CASE 3: pick L
                    if k < 2:
                        dp[i + 1][j][k + 1] = (
                            dp[i + 1][j][k + 1] + dp[i][j][k]
                        ) % to_mod
        return (
            dp[n][0][0]
            + dp[n][1][0]
            + dp[n][0][1]
            + dp[n][0][2]
            + dp[n][1][1]
            + dp[n][1][2]
        ) % to_mod
