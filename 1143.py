class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]
        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                max_val = -1
                if text1[i - 1] == text2[j - 1]:
                    max_val = max(max_val, dp[i - 1][j - 1] + 1)
                max_val = max(max_val, dp[i - 1][j], dp[i][j - 1])
                dp[i][j] = max_val
        return dp[len(text1)][len(text2)]
