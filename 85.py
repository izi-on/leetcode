class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n, m = len(matrix), len(matrix[0])
        height = [[0 for _ in range(m)] for _ in range(n)]

        for j in range(m):
            track = 0
            for i in range(n):
                track += 1
                if matrix[i][j] != "1":
                    track = 0
                height[i][j] = track

        tm = 0
        for i in range(n):
            stack = []
            for j in range(m):
                h = height[i][j]
                w = 1
                while stack and stack[-1][1] >= h:
                    cand = stack.pop()
                    w += cand[0]
                    tm = max(tm, (w - 1) * cand[1])
                stack.append((w, h))
                tm = max(tm, w * h)
            r = m
            l = r
            while stack:
                cur = stack.pop()
                l -= cur[0]
                tm = max(tm, (r - l) * cur[1])

        return tm
