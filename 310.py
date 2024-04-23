from collections import defaultdict, deque


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if len(edges) == 0:
            return [0]

        # create adj list and get potential leafs
        adj_list = defaultdict(set[int])
        for edge in edges:
            adj_list[edge[0]].add(edge[1])
            adj_list[edge[1]].add(edge[0])

        # get candidates for topo sort
        bfs = deque()
        for node, neighbours in adj_list.items():
            if len(neighbours) == 1:
                bfs.append(node)

        node_num = n

        # do topo sort
        while len(bfs) > 0:
            n = len(bfs)
            removed = False
            if node_num <= 2:
                break
            for _ in range(n):
                cur_node = bfs.popleft()
                node_num -= 1
                for neighbour in adj_list[cur_node]:
                    del adj_list[cur_node]
                    adj_list[neighbour].remove(cur_node)
                    removed = True
                    if len(adj_list[neighbour]) == 1:
                        bfs.append(neighbour)
            if not removed:
                break
        return [node for node in adj_list]
