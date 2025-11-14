class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        diff = [[0] * (n + 1) for _ in range(n + 1)]
        for query in queries:
            tl = [query[0], query[1]]
            br = [query[2], query[3]]
            diff[tl[0]][tl[1]] += 1
            diff[br[0] + 1][tl[1]] -= 1
            diff[tl[0]][br[1] + 1] -= 1
            diff[br[0] + 1][br[1] + 1] += 1

        ans = [[0] * (n) for _ in range(n)]
        for i in range(n):
            for j in range(n):
                above = ans[i - 1][j] if i - 1 >= 0 else 0
                left = ans[i][j - 1] if j - 1 >= 0 else 0
                above_left = ans[i - 1][j - 1] if i - 1 >= 0 and j - 1 >= 0 else 0
                ans[i][j] = diff[i][j] + above + left - above_left
        return ans
