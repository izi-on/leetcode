class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        n = row
        m = col + 2

        def coord_to_num(coord):
            i, j = coord
            return i * m + j

        p = [coord_to_num((i, j)) for i in range(n) for j in range(m)]
        r = [0 for _ in range(n) for _ in range(m)]

        def find(i):
            if i == p[i]:
                return i
            p[i] = find(p[i])
            return p[i]

        def union(coord1, coord2):
            a = coord_to_num(coord1)
            b = coord_to_num(coord2)

            pa = find(a)
            pb = find(b)

            if pa == pb:
                return

            if r[pa] < r[pb]:
                p[pa] = pb
                r[pb] += r[pa]
            else:
                p[pb] = pa
                r[pa] += r[pb]

        def check_done():
            coord1 = (0, 0)
            coord2 = (0, m - 1)
            return find(coord_to_num(coord1)) == find(coord_to_num(coord2))

        # init
        seen_cells = set()
        for i in range(1, row):
            coord1 = (i, 0)
            coord2 = (i - 1, 0)
            union(coord1, coord2)
            seen_cells.add((i - 1, 0))
            seen_cells.add((i, 0))

            coord1 = (i - 1, m - 1)
            coord2 = (i, m - 1)
            union(coord1, coord2)
            seen_cells.add((i - 1, m - 1))
            seen_cells.add((i, m - 1))

        deltas = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

        for k, cell in enumerate(cells):
            print("____")
            i, j = cell
            i -= 1
            seen_cells.add((i, j))
            for delta in deltas:
                id, jd = i + delta[0], j + delta[1]
                if (id, jd) in seen_cells:
                    print("union with", (i, j), (id, jd))
                    union((i, j), (id, jd))
                if check_done():
                    return k
