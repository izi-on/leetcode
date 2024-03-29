class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = set()
        s = "$" + s

        def dfs(i, j, star):
            if i == 0 and j == -1:
                return True
            if (i, j) in dp:
                return False
            try:
                if -1 in (i, j):
                    return False
                if s[i] == p[j] or p[j] == "." and s[i] != "$":
                    if star:
                        return dfs(i - 1, j, True) or dfs(i, j - 1, False)
                    else:
                        return dfs(i - 1, j - 1, False)
                if star:
                    return dfs(i, j - 1, False)
                if p[j] == "*":
                    return dfs(i, j - 1, True)
                return False
            finally:
                dp.add((i, j))

        return dfs(len(s) - 1, len(p) - 1, False)
