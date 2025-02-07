from collections import defaultdict


class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ans = []
        ball_to_col = {}
        col_count = defaultdict(int)
        cols = set()
        for query in queries:
            ball, col = query

            # if ball already assigned
            if ball in ball_to_col.keys():
                # old color handling
                old_col = ball_to_col[ball]
                col_count[old_col] -= 1
                if col_count[old_col] == 0:
                    cols.remove(old_col)

            # handle
            ball_to_col[ball] = col
            col_count[col] += 1
            cols.add(col)

            ans.append(len(cols))
        return ans
