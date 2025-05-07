from collections import deque


class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        bfs = deque()
        for i, domino in enumerate(dominoes):
            if domino != ".":
                if domino == "L" and i < len(dominoes) - 1:
                    bfs.append((i + 1, domino))
                elif domino == "R" and 0 < i:
                    bfs.append((i - 1, domino))

        dominoes_list = list(dominoes)

        while bfs:
            n = len(bfs)
            for _ in range(n):
                i, domino_expected = bfs.popleft()
                if dominoes_list[i] != ".":
                    dominoes_list[i] = "."
                    continue
                dominoes_list[i] = domino_expected
                change = 1 if domino_expected == "R" else -1
                new_pos = change + i
                if 0 <= new_pos < len(dominoes_list):
                    bfs.append((new_pos, domino_expected))

        return "".join(dominoes_list)
