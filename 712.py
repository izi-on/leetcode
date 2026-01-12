class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n = len(s1)
        m = len(s2)
        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        for i in range(n):
            dp[i][-1] = 0
        for i in range(m):
            dp[-1][i] = 0

        for i in range(n):
            for j in range(m):
                ans = dp[i][j - 1]

                ans = max(ans, dp[i - 1][j])

                if s1[i] == s2[j]:
                    ans = max(ans, dp[i - 1][j - 1] + ord(s1[i]))

                dp[i][j] = ans

        lcs = dp[n - 1][m - 1]

        return sum([ord(c) for c in s1]) - lcs + sum([ord(c) for c in s2]) - lcs
