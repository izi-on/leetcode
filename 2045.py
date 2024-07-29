from collections import defaultdict, deque


class Solution:
    def secondMinimum(
        self, n: int, edges: List[List[int]], time: int, change: int
    ) -> int:
        adj_list = defaultdict(set)
        for edge in edges:
            adj_list[edge[0]].add(edge[1])
            adj_list[edge[1]].add(edge[0])

        def bfs():
            nonlocal adj_list
            bfs = deque()
            bfs.append(1)
            visited_count = defaultdict(int)
            time_cur = 0
            cur_answer = None
            time_taken_for = defaultdict(lambda: -1)
            while len(bfs) > 0:
                # print("at time", time_cur)
                n_r = len(bfs)
                for _ in range(n_r):
                    node = bfs.popleft()
                    if visited_count[node] == 2:
                        continue
                    visited_count[node] += 1
                    if n == node and visited_count[node] == 1:
                        cur_answer = time_cur
                    if n == node and visited_count[node] == 2:
                        if time_cur == cur_answer:
                            visited_count[node] -= 1
                        else:
                            return time_cur
                    if visited_count[node] == 1:
                        time_taken_for[node] = time_cur
                    elif visited_count[node] == 2:
                        if time_taken_for[node] == time_cur:
                            visited_count[node] -= 1

                    for neighbor in adj_list[node]:
                        bfs.append(neighbor)
                if (time_cur // change) % 2 == 1:
                    # print("is red, waiting", change - (time_cur % change))
                    time_cur += change - (time_cur % change)
                time_cur += time
            return -1

        return bfs()
