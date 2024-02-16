class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def helper(i, j, visited):
            if (
                not (0 <= i < len(grid) and 0 <= j < len(grid[0]))
                or (i, j) in visited
                or grid[i][j] == 0
            ):
                return 0
            visited.add((i, j))
            deltas = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            area = sum(
                [helper(i + delta[0], j + delta[1], visited) for delta in deltas]
            )
            return area + 1

        visited = set()
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visited:
                    ans = max(ans, helper(i, j, visited))
        return ans
