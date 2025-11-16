class Solution:
    def numSub(self, s: str) -> int:
        start = 0
        ans = 0
        MOD = 10**9 + 7

        def count(length):
            return length * (length + 1) // 2

        for i, c in enumerate(s):
            if c == "0":
                ans += count(i - start)
                start = i + 1

        ans += count(len(s) - start)
        return ans % MOD
