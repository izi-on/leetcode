from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []

        def dfs(avail_cols, pos_diag, neg_diag, row_idx, cur_board: List[List[str]]):
            if row_idx == n:
                ans.append(cur_board.copy())

            for col in list(avail_cols):
                if (row_idx - col) in pos_diag or (row_idx + col) in neg_diag:
                    continue

                new_row = ["." for _ in range(n)]
                new_row[col] = "Q"
                new_row = "".join(new_row)

                avail_cols.remove(col)
                pos_diag.add(row_idx - col)
                neg_diag.add(row_idx + col)
                cur_board.append(new_row)

                dfs(avail_cols, pos_diag, neg_diag, row_idx + 1, cur_board)

                cur_board.pop()
                pos_diag.remove(row_idx - col)
                neg_diag.remove(row_idx + col)
                avail_cols.add(col)

        dfs({i for i in range(n)}, set(), set(), 0, [])
        return ans
