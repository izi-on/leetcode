class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        n, m = len(mat), len(mat[0])

        p_sum = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        for i in range(n):
            for j in range(m):
                p_sum[i][j] = (
                    (p_sum[i - 1][j] if i > 0 else 0)
                    + (p_sum[i][j - 1] if j > 0 else 0)
                    - (p_sum[i - 1][j - 1] if i > 0 and j > 0 else 0)
                ) + mat[i][j]

        def check(l):
            for i in range(n - l + 1):
                for j in range(m - l + 1):
                    s = (
                        p_sum[i + l - 1][j + l - 1]
                        - p_sum[i + l - 1][j - 1]
                        - p_sum[i - 1][j + l - 1]
                        + p_sum[i - 1][j - 1]
                    )
                    if s <= threshold:
                        return True
            return False

        l, r = 1, min(n, m)
        ans = 0
        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans
