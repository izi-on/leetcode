class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        deltas = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] != 1:
                    continue
                perimeter = 4
                for delta in deltas:
                    ic, jc = i + delta[0], j + delta[1]
                    if not (0 <= ic < n and 0 <= jc < m):
                        continue
                    if grid[ic][jc] == 1:
                        perimeter -= 1
                ans += perimeter
        return ans
