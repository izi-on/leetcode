class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        deltas = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        memoize = {}

        def get_max_path(cur, visited):
            if cur in visited:
                return 0
            gridVal = grid[cur[0]][cur[1]]
            if gridVal == 0:
                return 0
            gold = 0
            visited.add(cur)
            for delta in deltas:
                i_n, j_n = cur[0] + delta[0], cur[1] + delta[1]
                if not (0 <= i_n < len(grid) and 0 <= j_n < len(grid[0])):
                    continue
                gold = max(gold, get_max_path((i_n, j_n), visited))
            visited.remove(cur)
            return gold + gridVal

        most_gold = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                most_gold = max(
                    most_gold,
                    get_max_path(
                        (i, j),
                        set(),
                    ),
                )
        return most_gold
