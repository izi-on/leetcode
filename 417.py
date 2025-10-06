class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n, m = len(heights), len(heights[0])
        marked_node_pacific = set()
        marked_node_atlantic = set()

        deltas = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def in_bounds(cur):
            return 0 <= cur[0] < n and 0 <= cur[1] < m

        def get_n(cur):
            for delta in deltas:
                cand = (cur[0] + delta[0], cur[1] + delta[1])
                if in_bounds(cand):
                    yield cand

        def explore_mark(start, marked_set):
            if start in marked_set:
                return
            marked_set.add(start)
            for neighbour in get_n(start):
                i_s, j_s = start
                i_n, j_n = neighbour
                if heights[i_n][j_n] >= heights[i_s][j_s]:
                    explore_mark(neighbour, marked_set)

        for i in range(n):
            explore_mark((i, 0), marked_node_pacific)
        for j in range(m):
            explore_mark((0, j), marked_node_pacific)

        for i in range(n):
            explore_mark((i, m - 1), marked_node_atlantic)
        for j in range(m):
            explore_mark((n - 1, j), marked_node_atlantic)

        return list(marked_node_pacific.intersection(marked_node_atlantic))
