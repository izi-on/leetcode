class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        sum_left_to_right = []
        sum_right_to_left = [0 for _ in range(m)]
        total = 0
        for i in range(m):
            total += grid[1][i]
            sum_left_to_right.append(total)
        total = 0
        for i in range(m-1, -1, -1):
            total += grid[0][i]
            sum_right_to_left[i] = total


        ans = float("inf")
        for i in range(m):
            total = 0
            if i != 0:
                total = sum_left_to_right[i-1]
            if i != m-1:
                total = max(sum_right_to_left[i+1], total)
            ans = min(total, ans)
        return ans
