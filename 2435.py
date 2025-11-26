class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        MOD = 10**9 + 7

        n = len(grid)
        m = len(grid[0])
        dp = [[[0 for _ in range(k)] for _ in range(m)] for _ in range(n)]

        dp[n - 1][m - 1][grid[n - 1][m - 1] % k] = 1
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                val = grid[i][j]
                for rem in range(k):
                    if i + 1 < n:
                        dp[i][j][(val + rem) % k] = (
                            dp[i][j][(val + rem) % k] + dp[i + 1][j][rem]
                        ) % MOD
                    if j + 1 < m:
                        dp[i][j][(val + rem) % k] = (
                            dp[i][j][(val + rem) % k] + dp[i][j + 1][rem]
                        ) % MOD
        return dp[0][0][0]
