from collections import deque


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        deltas = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        def helper_discover(i, j):
            stack = deque()
            stack.append((i, j))
            visited = set()
            while len(stack) > 0:
                cur = stack.pop()
                if cur in visited:
                    continue
                i, j = cur
                if board[i][j] == "X":
                    continue
                if not (0 <= i < len(board) and 0 <= j < len(board[0])):
                    return False
                for delta in deltas:
                    stack.append((i + delta[0], j + delta[1]))
            return True

        def helper_flip(i, j):
            if board[i][j] == "X":
                return
            board[i][j] = "O"
            for delta in deltas:
                helper_flip(i + delta[0], j + delta[1])

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    if helper_discover(i, j):
                        helper_flip(i, j)
