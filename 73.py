class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        rowZero = False
        ROWS = len(matrix)
        COLS = len(matrix[0])
        for i in range(0, ROWS):
            for j in range(0, COLS):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    if i == 0:
                        rowZero = True
                    else:
                        matrix[i][0] = 0
        for i in range(1, ROWS):
            for j in range(1, COLS):
                if matrix[0][j] == 0:
                    matrix[i][j] = 0
                elif matrix[i][0] == 0:
                    matrix[i][j] = 0
        if matrix[0][0] == 0:
            for i in range(0, ROWS):
                matrix[i][0] = 0
        if rowZero:
            for i in range(0, COLS):
                matrix[0][i] = 0
