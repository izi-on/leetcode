from collections import defaultdict
import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        min_time = [float("infinity") for _ in range(n + 1)]
        adj_list = defaultdict(list)
        for source, dest, time in times:
            adj_list[source].append([time, dest])

        min_time[k] = 0
        min_heap = [[0, k]]
        track_time = 0
        visited = set()
        while min_heap:
            time, cur_node = heapq.heappop(min_heap)
            if cur_node in visited:
                continue
            visited.add(cur_node)
            track_time = max(track_time, time)
            for time_to_neighbour, neighbour in adj_list[cur_node]:
                if time + time_to_neighbour < min_time[neighbour]:
                    min_time[neighbour] = time + time_to_neighbour
                heapq.heappush(min_heap, [min_time[neighbour], neighbour])
        return track_time if len(visited) == n else -1
