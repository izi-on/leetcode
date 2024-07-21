from collections import deque
import heapq


class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        answer = [[0] * len(colSum) for _ in range(len(rowSum))]
        hq: list[tuple[int, int]] = []
        for i, r in enumerate(rowSum):
            heapq.heappush(hq, (r, i))
        cur_col_val = {}
        col_heap = []
        for i, c in enumerate(colSum):
            heapq.heappush(col_heap, (c, i))
            cur_col_val[i] = c
        while hq:
            val, r_idx = heapq.heappop(hq)
            while val != 0:
                c_val, c_idx = heapq.heappop(col_heap)
                while c_val != cur_col_val[c_idx] or c_val <= 0:
                    c_val, c_idx = heapq.heappop(col_heap)
                to_remove = min(val, c_val)
                val -= to_remove
                c_val -= to_remove
                cur_col_val[c_idx] = c_val
                if c_val > 0:
                    heapq.heappush(col_heap, (c_val, c_idx))
                answer[r_idx][c_idx] = to_remove
        return answer
