from collections import deque


class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        n = len(mat)
        m = len(mat[0])
        rows = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            prev = 0
            for j in range(m):
                if mat[i][j] == 0:
                    prev = 0
                rows[i][j] = prev + mat[i][j]
                prev = rows[i][j]

        print(rows)
        ans = 0

        for j in range(m):
            stack = []
            total = 0
            for i in range(n):
                width = rows[i][j]
                cnt = 1
                while stack and stack[-1][0] >= width:
                    w, c = stack.pop()
                    total -= w * c
                    cnt += c
                total += width * cnt
                stack.append((width, cnt))
                ans += total
        return ans
