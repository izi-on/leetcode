class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0 for _ in s]
        if s[0] == "0":
            return 0
        if len(s) == 1:
            return 1 if s[0] != "0" else 0
        dp[0] = 1

        dp[1] = dp[0] if s[1] != "0" else 0
        dp[1] += 1 if 1 <= int(s[:2]) <= 26 else 0

        for i in range(2, len(s)):
            dp[i] = dp[i - 1] if s[i] != "0" else 0
            dp[i] += (
                dp[i - 2] if s[i - 1] != "0" and 1 <= int(s[i - 1 : i + 1]) <= 26 else 0
            )

        return dp[len(s) - 1]
