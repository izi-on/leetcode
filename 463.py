class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        deltas = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        perimeter = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    continue
                for delta in deltas:
                    i_n = i + delta[0]
                    j_n = j + delta[1]
                    if not (0 <= i_n < len(grid) and 0 <= j_n < len(grid[0])) or (
                        grid[i_n][j_n] == 0
                    ):
                        perimeter += 1
        return perimeter
