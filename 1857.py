from collections import defaultdict, deque


class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)

        adj = defaultdict(set)
        adj_track = defaultdict(set)
        rev_adj = defaultdict(set)
        for edge in edges:
            adj[edge[0]].add(edge[1])
            adj_track[edge[0]].add(edge[1])
            rev_adj[edge[1]].add(edge[0])

        # find cycles
        visited = set()

        def helper(cur_node, rec_stack):
            nonlocal visited
            if cur_node in visited:
                return False
            if cur_node in rec_stack:
                return True
            rec_stack.add(cur_node)
            for nb in adj[cur_node]:
                if helper(nb, rec_stack):
                    return True
            visited.add(cur_node)
            rec_stack.remove(cur_node)
            return False

        for i in range(n):
            if i not in visited and helper(i, set()):
                return -1

        # get all sinks
        sinks = set(range(n))
        for k, v in adj_track.items():
            if len(v) != 0:
                sinks.remove(k)

        bfs = deque(list(sinks))
        dp = defaultdict(lambda: defaultdict(int))
        ans = 0
        while bfs:
            cur_node = bfs.popleft()
            for nb in adj[cur_node]:
                for color in dp[nb].keys():
                    dp[cur_node][color] = max(dp[cur_node][color], dp[nb][color])
            dp[cur_node][colors[cur_node]] += 1

            # find max if it exists
            for _, v in dp[cur_node].items():
                ans = max(ans, v)

            # find next
            for nb in rev_adj[cur_node]:
                adj_track[nb].remove(cur_node)
                if len(adj_track[nb]) == 0:
                    bfs.append(nb)
        return ans
