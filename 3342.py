from collections import defaultdict
import heapq


class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        def helper(i, j):
            return 1 if (i + j) % 2 == 0 else 2

        n, m = len(moveTime), len(moveTime[0])
        heap = [(0, 0, 0)]
        d = set()
        visit = defaultdict(lambda: float("inf"))
        deltas = [[0, -1], [0, 1], [1, 0], [-1, 0]]
        while heap:
            time, i, j = heapq.heappop(heap)
            if (i, j) in d:
                continue
            d.add((i, j))
            # print(i,j,time)
            visit[(i, j)] = time
            for delta in deltas:
                i_n, j_n = i + delta[0], j + delta[1]
                if not (0 <= i_n < n and 0 <= j_n < m):
                    continue
                time_n = max(time, moveTime[i_n][j_n]) + helper(i, j)
                if visit[(i_n, j_n)] > time_n:
                    heapq.heappush(heap, (time_n, i_n, j_n))
        return visit[(n - 1, m - 1)]
