from collections import defaultdict, deque
import heapq


class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        adj_list = defaultdict(list)
        for flight in flights:
            adj_list[flight[0]].append((flight[1], flight[2]))
        min_price = [float("infinity") for _ in range(n)]
        stop_at = [float("infinity") for _ in range(n)]
        min_price[src] = 0
        stop_at[src] = 0
        bfs = [(0, src, -1)]
        heapq.heapify(bfs)
        while len(bfs) > 0:
            price, cur, stop = heapq.heappop(bfs)
            print(price, cur, stop)
            if cur == dst:
                return price
            if stop == k:
                continue
            for neighbor, p_to_n in adj_list[cur]:
                if price + p_to_n < min_price[neighbor] or stop + 1 < stop_at[neighbor]:
                    min_price[neighbor] = price + p_to_n
                    stop_at[neighbor] = stop + 1
                    heapq.heappush(bfs, (price + p_to_n, neighbor, stop + 1))
        return -1
