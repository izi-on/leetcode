from collections import deque


class Solution:
    deltas = [[-1, 0], [1, 0], [0, 1], [0, -1]]

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def get_tiles(prev, cur, visited):
            i, j = cur
            if (
                cur in visited
                or (not (0 <= i < len(heights) and 0 <= j < len(heights[0])))
                or prev > heights[i][j]
            ):
                return []
            visited.add(cur)

            tiles = [(i, j)]
            for delta in Solution.deltas:
                tiles += get_tiles(heights[i][j], (i + delta[0], j + delta[1]), visited)
            return tiles

        # do pacific
        p = []
        for i in range(1, len(heights)):
            p.append((i, 0))
        for i in range(len(heights[0])):
            p.append((0, i))
        visited = set()
        p_tiles = []
        for tile in p:
            p_tiles += get_tiles(-1, tile, visited)

        # do altantic
        a = []
        for i in range(0, len(heights) - 1):
            a.append((i, len(heights[0]) - 1))
        for i in range(len(heights[0])):
            a.append((len(heights) - 1, i))
        visited = set()
        a_tiles = []
        for tile in a:
            a_tiles += get_tiles(-1, tile, visited)

        ans = set(a_tiles).intersection(set(p_tiles))
        return list(map(lambda x: list(x), ans))
