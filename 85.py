class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # get heights
        n, m = len(matrix), len(matrix[0])
        heights = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(m):
                if i == n - 1 and matrix[i][j] == "1":
                    heights[i][j] = 1
                    continue
                if matrix[i][j] == "0":
                    heights[i][j] = 0
                else:
                    heights[i][j] = 1 + heights[i + 1][j]

        # solve rectangle histogram for each row
        max_rect = 0
        for row in range(n):
            stack = []
            height = heights[row]
            for col in range(m):
                start_col = col
                while stack and stack[-1][1] >= height[col]:
                    rect = stack.pop()
                    max_rect = max(max_rect, (col - rect[0]) * rect[1])
                    start_col = rect[0]
                stack.append((start_col, height[col]))
            while stack:
                rect = stack.pop()
                max_rect = max(max_rect, rect[1] * (m - rect[0]))
        return max_rect
