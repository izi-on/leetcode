from collections import defaultdict
import heapq


class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        adj_list = defaultdict(set)
        for edge in edges:
            u, v, w = edge
            adj_list[u].add((v, w))
            adj_list[v].add((u, 2 * w))

        track = {}
        heap = [(0, 0)]

        while heap:
            w, u = heapq.heappop(heap)
            if u in track:
                continue
            track[u] = w
            for nb in adj_list[u]:
                nu, nw = nb
                if nu in track:
                    continue
                heapq.heappush(heap, (nw + w, nu))

        return track.get(n - 1) or -1
