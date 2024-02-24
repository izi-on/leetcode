from collections import deque


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        bfs = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    bfs.append((i, j))
        visited = set()
        deltas = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        lvl = 0
        while len(bfs) > 0:
            n = len(bfs)
            for _ in range(n):
                i, j = bfs.popleft()
                if (
                    not (0 <= i < len(grid) and 0 <= j < len(grid[0]))
                    or (i, j) in visited
                    or grid[i][j] == -1
                ):
                    continue
                visited.add((i, j))
                grid[i][j] = min(grid[i][j], lvl)
                for delta in deltas:
                    bfs.append((i + delta[1], j + delta[1]))
            lvl += 2
        return grid
