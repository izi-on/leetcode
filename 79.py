class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        deltas = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(i, j, idx, visited):
            if idx == len(word):
                return True
            if (
                (i, j) in visited
                or 0 > i
                or i >= len(board)
                or 0 > j
                or j >= len(board[i])
                or board[i][j] != word[idx]
            ):
                return False
            visited.add((i, j))
            for delta in deltas:
                n_i = i + delta[0]
                n_j = j + delta[1]
                if dfs(n_i, n_j, idx + 1, visited):
                    return True
            visited.remove((i, j))
            return False

        for i, _ in enumerate(board):
            for j, _ in enumerate(board[i]):
                if dfs(i, j, 0, set()):
                    return True
        return False
