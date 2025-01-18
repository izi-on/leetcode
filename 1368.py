class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dp = [[float("inf") for _ in range(m)] for _ in range(n)]
        dp[0][0] = 0
        change = True
        while change:
            change = False
            # parse from top-left
            for i in range(n):
                for j in range(m):
                    # option 1: get from left side
                    prev_val = dp[i][j]
                    cur_best = float("inf")
                    if j > 0:
                        cost = 0 if grid[i][j - 1] == 1 else 1
                        cur_best = min(cur_best, dp[i][j - 1] + cost)

                    # option 2: get from top
                    if i > 0:
                        cost = 0 if grid[i - 1][j] == 3 else 1
                        cur_best = min(cur_best, dp[i - 1][j] + cost)
                    dp[i][j] = min(dp[i][j], cur_best)
                    if dp[i][j] != prev_val:
                        change = True

            # parse from top-left
            for i in range(n - 1, -1, -1):
                for j in range(m - 1, -1, -1):
                    # option 1: get from right side
                    prev_val = dp[i][j]
                    cur_best = float("inf")
                    if j < m - 1:
                        cost = 0 if grid[i][j + 1] == 2 else 1
                        cur_best = min(cur_best, dp[i][j + 1] + cost)

                    # option 2: get from bottom
                    if i < n - 1:
                        cost = 0 if grid[i + 1][j] == 4 else 1
                        cur_best = min(cur_best, dp[i + 1][j] + cost)
                    dp[i][j] = min(dp[i][j], cur_best)
                    if dp[i][j] != prev_val:
                        change = True
        return dp[-1][-1]
