class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        row_count = [0 for _ in range(n)]
        col_count = [0 for _ in range(m)]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    row_count[i] += 1
                    col_count[j] += 1

        count = 0
        for i in range(n):
            for j in range(m):
                if not (row_count[i] > 1 or col_count[j] > 1):
                    continue
                if grid[i][j] == 1:
                    count += 1
        return count
