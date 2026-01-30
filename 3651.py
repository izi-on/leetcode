class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        n = len(grid)
        m = len(grid[0])
        dp = [[float("inf") for _ in range(m)] for _ in range(n)]
        tp = sorted([(grid[i][j], i, j) for i in range(n) for j in range(m)])
        for _ in range(k + 1):
            p1 = 0
            min_cost = float("inf")
            for p2 in range(len(tp)):
                p1_v = tp[p1][0]
                p2_v = tp[p2][0]
                i2, j2 = tp[p2][1], tp[p2][2]
                prev_min = min_cost
                min_cost = min(min_cost, dp[i2][j2])
                if p1_v == p2_v:
                    continue
                for r in range(p1, p2):
                    _, i, j = tp[r]
                    dp[i][j] = prev_min
                p1 = p2
            for r in range(p1, len(tp)):
                _, i, j = tp[r]
                dp[i][j] = min_cost

            for i in range(n - 1, -1, -1):
                for j in range(m - 1, -1, -1):
                    if i == n - 1 and j == m - 1:
                        dp[i][j] = 0
                        continue
                    dp[i][j] = min(
                        dp[i][j],
                        dp[i + 1][j] + grid[i + 1][j] if i + 1 < n else float("inf"),
                    )
                    dp[i][j] = min(
                        dp[i][j],
                        dp[i][j + 1] + grid[i][j + 1] if j + 1 < m else float("inf"),
                    )
        return dp[0][0]
