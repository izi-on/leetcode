from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        numOfOranges = sum([item for sublist in grid for item in sublist if item == 1])
        bfs = deque()
        deltas = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    bfs.append((i, j))
        if len(bfs) == 0 and numOfOranges == 0:
            return 0
        time = 0
        visited = set()
        while len(bfs) > 0:
            n = len(bfs)
            for _ in range(n):
                i, j = bfs.popleft()
                if not (0 <= i < len(grid) and 0 <= j < len(grid[0])):
                    continue
                if (i, j) in visited:
                    continue
                if grid[i][j] == 0:
                    continue
                visited.add((i, j))
                if grid[i][j] == 1:
                    numOfOranges -= 1
                if numOfOranges == 0:
                    return time
                grid[i][j] = 2
                for delta in deltas:
                    bfs.append((i + delta[0], j + delta[1]))
            time += 1
        return -1
