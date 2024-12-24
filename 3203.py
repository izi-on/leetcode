from collections import defaultdict, deque
from typing import List


class Solution:
    def find_diameter(self, edges: List[List[int]]):
        adj = defaultdict(set)
        for edge in edges:
            adj[edge[0]].add(edge[1])
            adj[edge[1]].add(edge[0])

        toposort = deque()
        count = len(adj.keys())
        path = 0
        for v, l in adj.items():
            if len(l) == 1:
                toposort.append(v)

        while count > 2:
            n = len(toposort)
            for _ in range(n):
                cur = toposort.popleft()
                count -= 1
                for node in adj[cur]:
                    adj[node].remove(cur)
                    if len(adj[node]) == 1:
                        toposort.append(node)
                del adj[cur]
            path += 1
        full_path = path * 2
        if count == 2:
            path += 1
            full_path += 1
        return path, full_path

    def minimumDiameterAfterMerge(
        self, edges1: List[List[int]], edges2: List[List[int]]
    ) -> int:
        t1, full_path_1 = self.find_diameter(edges1)
        t2, full_path_2 = self.find_diameter(edges2)
        return max([t1 + t2 + 1, full_path_1, full_path_2])
