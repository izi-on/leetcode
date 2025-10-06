class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        def in_bounds(cur):
            return 0 <= cur[0] < n and 0 <= cur[1] < m

        deltas = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        def get_n(cur):
            for delta in deltas:
                cand = (cur[0] + delta[0], cur[1] + delta[1])
                if in_bounds(cand):
                    yield cand

        def is_reachable(cur, height, visited):
            if cur == (n - 1, m - 1):
                return True

            if grid[cur[0]][cur[1]] > height:
                return False

            if cur in visited:
                return False
            visited.add(cur)

            possible_neighbours = list(
                filter(lambda ne: grid[ne[0]][ne[1]] <= height, list(get_n(cur)))
            )

            return any(
                [is_reachable(ne, height, visited) for ne in possible_neighbours]
            )

        l, r = 0, max(max(row) for row in grid)
        ans = -1
        while l <= r:
            mid = (l + r) // 2
            if is_reachable((0, 0), mid, set()):
                r = mid - 1
                ans = mid
            else:
                l = mid + 1
        return ans
