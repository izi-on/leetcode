class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top_left, bottom_right = [0, 0], [len(matrix) - 1, len(matrix[0]) - 1]
        trace = []
        while top_left[0] <= bottom_right[0] and top_left[1] <= bottom_right[1]:
            print(top_left, bottom_right)
            for i in range(top_left[1], bottom_right[1] + 1):
                print(matrix[top_left[0]][i])
                trace.append(matrix[top_left[0]][i])
            for i in range(top_left[0] + 1, bottom_right[0] + 1):
                print(matrix[i][bottom_right[1]])
                trace.append(matrix[i][bottom_right[1]])
            for i in range(bottom_right[1] - 1, top_left[1] - 1, -1):
                print(matrix[bottom_right[0]][i])
                trace.append(matrix[bottom_right[0]][i])
            for i in range(bottom_right[0] - 1, top_left[0], -1):
                print(matrix[i][top_left[1]])
                trace.append(matrix[i][top_left[1]])
            top_left = [top_left[0] + 1, top_left[1] + 1]
            bottom_right = [bottom_right[0] - 1, bottom_right[1] - 1]
        return trace
