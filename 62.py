class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def nChoseK(n, k):
            ans = 1
            a = k
            b = n - k
            a, b = max(a, b), min(a, b)
            for i in range(a + 1, n + 1):
                ans *= i
            for i in range(b + 1):
                ans //= i
            return ans

        return nChoseK(m + n - 2, m - 1)
