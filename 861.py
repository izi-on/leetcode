class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        def flip_row(i: int):
            for k in range(len(grid[i])):
                grid[i][k] = 1 - grid[i][k]

        def flip_column(i):
            for k in range(len(grid)):
                grid[k][i] = 1 - grid[k][i]

        # step 1: make all 1s in the beginning
        for i in range(len(grid)):
            row = grid[i]
            if row[0] == 0:
                flip_row(i)

        # flip columns if better value
        cols = list(zip(*grid))
        for i in range(len(cols)):
            column = cols[i]
            s_c = sum(column)
            if s_c < len(grid) - s_c:
                flip_column(i)

        # get binary sum
        binary_val = 0
        for row in grid:
            # print("".join(list(map(str, row))))
            binary_val += int("".join(list(map(str, row))), 2)

        return binary_val
