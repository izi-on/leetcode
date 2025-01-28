class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        visited = set()
        adj_cells = [(0, -1), (0, 1), (1, 0), (-1, 0)]

        def dfs(pos):
            if pos in visited:
                return 0
            visited.add(pos)
            i, j = pos
            if not (0 <= i < n and 0 <= j < m):
                return 0
            if grid[i][j] == 0:
                return 0
            count = grid[i][j]
            for adj in adj_cells:
                count += dfs((i + adj[0], j + adj[1]))
            return count

        max_count = 0
        for i in range(n):
            for j in range(m):
                get_count = dfs((i, j))
                max_count = max(get_count, max_count)
        return max_count
