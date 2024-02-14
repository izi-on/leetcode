from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        deltas = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        visited = set()

        def dfs(i, j):
            if (
                (i, j) in visited
                or not (0 <= i < len(grid) and 0 <= j < len(grid[0]))
                or not grid[i][j] == "1"
            ):
                return
            visited.add((i, j))
            for delta in deltas:
                dfs(i + delta[0], j + delta[1])

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visited and grid[i][j] == "1":
                    count += 1
                    dfs(i, j)
        return count
