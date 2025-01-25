from collections import deque
from collections import defaultdict


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        rev_adj_list = defaultdict(set)
        adj_list = defaultdict(set)
        n = len(graph)
        sinks = set([i for i in range(n)])
        for i in range(n):
            node = i
            adj_list[node].update(graph[i])
            for neighbour in graph[i]:
                rev_adj_list[neighbour].add(node)
                sinks.discard(node)

        sinks = deque(list(sinks))
        ans = sinks.copy()
        while sinks:
            cur = sinks.popleft()
            for neighbour in rev_adj_list[cur]:
                adj_list[neighbour].discard(cur)
                if len(adj_list[neighbour]) == 0:
                    sinks.append(neighbour)
                    ans.append(neighbour)

        return sorted(list(ans))
