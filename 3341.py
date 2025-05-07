import heapq
from collections import defaultdict
from typing import List


class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])
        deltas = [[0, -1], [0, 1], [1, 0], [-1, 0]]
        heap = []
        visited = defaultdict(lambda: float("inf"))
        d = set()
        heapq.heappush(heap, (0, 0, 0))
        while heap:
            unit = heapq.heappop(heap)
            time, i, j = unit
            if (i, j) in d:
                continue
            d.add((i, j))
            if visited[(i, j)] < max(time, moveTime[i][j] + 1):
                continue
            visited[(i, j)] = max(time, moveTime[i][j] + 1)
            for delta in deltas:
                i_n = i + delta[0]
                j_n = j + delta[1]
                if not (0 <= i_n < n and 0 <= j_n < m):
                    continue
                if visited[(i_n, j_n)] > max(time + 1, moveTime[i_n][j_n] + 1):
                    heapq.heappush(
                        heap, (max(time + 1, moveTime[i_n][j_n] + 1), i_n, j_n)
                    )
        return visited[(n - 1, m - 1)]
