import heapq


class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        map_int_to_delta = {1: [0, 1], 2: [0, -1], 3: [-1, 0], 4: [1, 0]}

        deltas = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def is_coordinate_in_bounds(i, j):
            return 0 <= i < n and 0 <= j < m

        cost_dict = {}  # map (start_coord, end_coord) to cost
        for i in range(n):
            for j in range(m):
                cur_coord = (i, j)
                for delta in deltas:
                    neighbour_coord = (i + delta[0], j + delta[1])
                    if not is_coordinate_in_bounds(*neighbour_coord):
                        continue
                    cost_dict[(cur_coord, neighbour_coord)] = 1 - (
                        delta == map_int_to_delta[grid[i][j]]
                    )

        # run djikstra
        cost_from_source = {}
        for i in range(n):
            for j in range(m):
                cost_from_source[(i, j)] = float("inf")
        cost_from_source[(0, 0)] = 0
        lowest_cost_heap = [(0, (0, 0))]
        visited = set()

        while lowest_cost_heap:
            _, cur_coord = heapq.heappop(lowest_cost_heap)
            if cur_coord in visited:
                continue
            visited.add(cur_coord)
            i, j = cur_coord
            for delta in deltas:
                neighbour_coord = (i + delta[0], j + delta[1])
                if not is_coordinate_in_bounds(*neighbour_coord):
                    continue
                cost_from_source[neighbour_coord] = min(
                    cost_from_source[neighbour_coord],
                    cost_from_source[cur_coord]
                    + cost_dict[(cur_coord, neighbour_coord)],
                )
                heapq.heappush(
                    lowest_cost_heap,
                    (cost_from_source[neighbour_coord], neighbour_coord),
                )

        return cost_from_source[(n - 1, m - 1)]
