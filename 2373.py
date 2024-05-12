class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        answer = []
        for i in range(1, n - 1):
            row = []
            for j in range(1, n - 1):
                max_val = 0
                for k in range(0, 3):
                    for k2 in range(0, 3):
                        max_val = max(max_val, grid[i - 1 + k][j - 1 + k2])
                row.append(max_val)
            answer.append(row)
        return answer
