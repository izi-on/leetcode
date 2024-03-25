class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        cache = {}

        def dfs(i, j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            if s[i] != t[j]:
                return dfs(i + 1, j)
            if (i, j) in cache:
                return cache[(i, j)]
            ways = dfs(i + 1, j + 1)
            ways += dfs(i + 1, j)
            cache[(i, j)] = ways
            return cache[(i, j)]

        return dfs(0, 0)
