from copy import copy


class Node:
    def __init__(self, val=None):
        self.val = val
        self.adj = {}
        self.is_end = False


class Solution:
    def __init__(self):
        self.root = Node()
        self.ans = set()

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        for word in words:
            ptr = self.root
            for c in word:
                if c not in ptr.adj:
                    node = Node(c)
                    ptr.adj[c] = node
                ptr = ptr.adj[c]
            ptr.is_end = True

        deltas = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(i, j, visited, ptr, word):
            if (
                not 0 <= i < len(board)
                or not 0 <= j < len(board[i])
                or board[i][j] not in ptr.adj
                or (i, j) in visited
            ):
                return

            visited.add((i, j))
            word.append(board[i][j])

            ptr = ptr.adj[board[i][j]]
            if ptr.is_end:
                self.ans.add("".join(word))
            for delta in deltas:
                i_n = i + delta[0]
                j_n = j + delta[1]
                dfs(i_n, j_n, visited, ptr, word)

            word.pop()
            visited.remove((i, j))

        for i in range(len(board)):
            for j in range(len(board[i])):
                dfs(i, j, set(), self.root, [])

        return list(self.ans)
