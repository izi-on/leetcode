from collections import deque
import heapq


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        n = len(heightMap)
        m = len(heightMap[0])

        filled = set()
        answer = 0
        border_spill_nodes = set()

        def tuple_wall_order(i, j):
            return (heightMap[i][j] if in_bounds(i, j) else -1, i, j)

        def get_neighbours(i, j):
            return [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]

        def in_bounds(i, j):
            return 0 <= i < n and 0 <= j < m

        def contains_out_of_bounds(neighbours):
            return any([not in_bounds(*neighbour) for neighbour in neighbours])

        def fill(i_s, j_s):
            nonlocal answer

            # ----init----
            filled.add((i_s, j_s))
            walls = get_neighbours(i_s, j_s)
            if contains_out_of_bounds(walls):
                return
            if (i_s, j_s) in border_spill_nodes:
                return
            walls_heap = [tuple_wall_order(i, j) for i, j in walls]
            heapq.heapify(walls_heap)
            current_covered_cells = set([(i_s, j_s)])
            height_of_covered = heightMap[i_s][j_s]
            bound_height = height_of_covered
            # -------------

            while walls_heap:
                print("bruh2")
                height, i, j = heapq.heappop(walls_heap)
                if (i, j) in border_spill_nodes:
                    answer += (height - height_of_covered) * len(current_covered_cells)
                    return

                # add to filled, dont explore again
                filled.add((i, j))

                # check if new biggest height
                bound_height = max(bound_height, height)

                # add extra height if necessary
                answer += bound_height - height

                answer += (bound_height - height_of_covered) * len(
                    current_covered_cells
                )
                current_covered_cells.add((i, j))
                height_of_covered = bound_height
                for neighbour in get_neighbours(i, j):
                    if neighbour not in current_covered_cells:
                        heapq.heappush(
                            walls_heap, tuple_wall_order(neighbour[0], neighbour[1])
                        )

        def mark_border_spill_nodes(i_s, j_s):
            if (i_s, j_s) in border_spill_nodes:
                return
            heap = [tuple_wall_order(i_s, j_s)]
            heapq.heapify(heap)
            prev_height = -1
            while heap:
                print("bruh3")
                height, i, j = heapq.heappop(heap)
                if not in_bounds(i, j):
                    continue
                if prev_height > height:
                    continue
                if (i, j) in border_spill_nodes:
                    continue
                border_spill_nodes.add((i, j))
                prev_height = height
                for neighbour in get_neighbours(i, j):
                    heapq.heappush(heap, tuple_wall_order(*neighbour))

        to_explore = [tuple_wall_order(i, j) for i in range(n) for j in range(m)]
        heapq.heapify(to_explore)

        for i in range(n):
            mark_border_spill_nodes(i, 0)
            mark_border_spill_nodes(i, m - 1)
        for j in range(m):
            mark_border_spill_nodes(0, j)
            mark_border_spill_nodes(n - 1, j)

        while to_explore:
            print("bruh")
            _, i, j = heapq.heappop(to_explore)
            if (i, j) in filled:
                continue
            fill(i, j)
