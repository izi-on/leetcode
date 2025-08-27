class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        deltas = [(1, -1), (-1, -1), (-1, 1), (1, 1)]
        n = len(grid)
        m = len(grid[0])
        ans = 0

        mem = {}

        def attempt(i, j, dir, cur_len, turns, prev):
            if not (0 <= i < n and 0 <= j < m):
                return 0

            if (i, j, dir, turns, prev) in mem:
                return mem[(i, j, dir, turns, prev)]

            max_ans = 0

            if not dir:  # at 1
                for delta in deltas:
                    max_ans = max(
                        max_ans,
                        attempt(i + delta[0], j + delta[1], delta, cur_len + 1, 0, 0)
                        + 1,
                    )
                return max_ans

            if (prev == 0 and grid[i][j] == 2) or (prev == 2 and grid[i][j] == 0):
                if turns == 0:
                    new_dir = deltas[(deltas.index(dir) + 1) % 4]
                    max_ans = max(
                        attempt(
                            i + new_dir[0],
                            j + new_dir[1],
                            new_dir,
                            cur_len + 1,
                            turns + 1,
                            grid[i][j],
                        )
                        + 1,
                        max_ans,
                    )
                max_ans = max(
                    max_ans,
                    attempt(i + dir[0], j + dir[1], dir, cur_len + 1, turns, grid[i][j])
                    + 1,
                )
            mem[(i, j, dir, turns, prev)] = max_ans
            return max_ans

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    ans = max(ans, attempt(i, j, None, 0, 0, 0))

        return ans
