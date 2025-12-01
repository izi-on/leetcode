from collections import deque
from typing import List


class Solution:
    def maxKDivisibleComponents(
        self, n: int, edges: List[List[int]], values: List[int], k: int
    ) -> int:
        adj_list = [set() for _ in range(n)]
        rem = [values[i] % k for i in range(n)]
        for e in edges:
            e1, e2 = e
            adj_list[e1].add(e2)
            adj_list[e2].add(e1)

        leafs = [i for i in range(n) if len(adj_list[i]) == 1]
        bfs = deque(leafs)
        ans = 0
        while bfs:
            node = bfs.popleft()
            has_parent = False
            for pn in adj_list[node]:
                has_parent = True
                rem[pn] = (rem[pn] + rem[node]) % k
                adj_list[pn].remove(node)
                if len(adj_list[pn]) <= 1:
                    bfs.append(pn)

            if rem[node] == 0 and has_parent:
                ans += 1
        return ans + 1  # was counting split, and each split is one extra component
