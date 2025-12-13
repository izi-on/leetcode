from collections import defaultdict
import bisect


class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        i_to_row = defaultdict(list)
        j_to_col = defaultdict(list)

        for building in sorted(buildings):
            i, j = building
            i_to_row[i].append(j)
            j_to_col[j].append(i)

        count = 0
        for building in buildings:
            i, j = building
            row = i_to_row[i]
            idx = bisect.bisect_left(row, j)
            if idx == 0 or idx == len(row) - 1:
                continue
            col = j_to_col[j]
            idx = bisect.bisect_left(col, i)
            if idx == 0 or idx == len(col) - 1:
                continue
            count += 1
        return count
