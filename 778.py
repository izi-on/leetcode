from collections import deque
import heapq


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        start = (0, 0)
        track_max_along_path = {
            (i, j): float("infinity")
            for i in range(len(grid))
            for j in range(len(grid))
        }
        track_max_along_path[(0, 0)] = grid[0][0]
        bfs = [(grid[0][0], start)]
        visited = set()
        deltas = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        while len(bfs):
            cur_max, (i, j) = heapq.heappop(bfs)
            if (i, j) in visited:
                continue
            visited.add((i, j))
            for delta in deltas:
                i_n = i + delta[0]
                j_n = j + delta[1]
                if not (0 <= i_n < len(grid) and 0 <= j_n < len(grid)):
                    continue
                candidate_value = max(cur_max, grid[i_n][j_n])
                if candidate_value >= track_max_along_path[(i_n, j_n)]:
                    continue
                track_max_along_path[(i_n, j_n)] = candidate_value
                heapq.heappush(bfs, (candidate_value, (i_n, j_n)))
        return track_max_along_path[(len(grid) - 1, len(grid) - 1)]
