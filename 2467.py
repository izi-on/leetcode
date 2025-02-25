from collections import defaultdict, deque


class Solution:
    def mostProfitablePath(
        self, edges: List[List[int]], bob: int, amount: List[int]
    ) -> int:
        adj_list = defaultdict(list)
        rev_adj_list = defaultdict(list)
        for edge in edges:
            u, v = edge
            adj_list[u].append(v)
            adj_list[v].append(u)

        def helper(path):
            if path[-1] == bob:
                return path[::-1]
            for a in adj_list[path[-1]]:
                if len(path) > 1 and a == path[-2]:
                    continue
                path.append(a)
                res = helper(path)
                if res:
                    return res
                path.pop()
            return []

        bob_path = helper([0])

        bfs = deque([(0, 0, None)])
        max_score = -float("inf")
        bob_path_idx = 0
        while bfs:
            bob_cur = bob_path[bob_path_idx]
            n = len(bfs)
            # print("__________")
            for _ in range(n):
                cur = bfs.popleft()
                # print(cur, "bob cur: ", bob_cur)
                val, node, prev = cur
                leaf = True
                if bob_cur == node:
                    val += amount[node] // 2
                else:
                    val += amount[node]
                for a in adj_list[node]:
                    if a == prev:
                        continue
                    bfs.append((val, a, node))
                    leaf = False
                if leaf:
                    max_score = max(max_score, val)
                amount[node] = 0
            # print("__________")
            amount[bob_cur] = 0
            bob_path_idx = min(bob_path_idx + 1, len(bob_path) - 1)
        return max_score
