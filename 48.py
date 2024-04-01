class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r = 0, len(matrix) - 1
        while l < r:
            for i in range(0, r - l):
                tmp = matrix[l][l + i]
                tmp, matrix[l + i][r] = matrix[l + i][r], tmp
                # tmp2 = matrix[l + i][r]
                # matrix[l + i][r] = tmp
                # tmp = tmp2
                tmp, matrix[r][r - i] = matrix[r][r - i], tmp
                # tmp2 = matrix[r][r - i]
                # matrix[r][r - i] = tmp
                # tmp = tmp2
                tmp, matrix[r - i][l] = matrix[r - i][l], tmp
                # tmp2 = matrix[r - i][l]
                # matrix[r - i][l] = tmp
                # tmp = tmp2
                tmp, matrix[l][l + i] = matrix[l][l + i], tmp
                # tmp2 = matrix[l][l + i]
                # matrix[l][l + i] = tmp
                # tmp = tmp2

            l += 1
            r -= 1
