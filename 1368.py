from functools import defaultdict
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        # created weighted graph
        n = len(grid)
        m = len(grid[0])
        adj_list = defaultdict(list)
        for i in range(n):
            for j in range(m):

