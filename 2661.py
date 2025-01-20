class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        n = len(mat)
        m = len(mat[0])
        id_to_coord = {}
        for i in range(n):
            for j in range(m):
                cell = mat[i][j]
                id_to_coord[cell] = (i, j)

        rows = [0 for _ in range(n)]
        cols = [0 for _ in range(m)]
        for k in range(len(arr)):
            to_fill_id = arr[k]
            i, j = id_to_coord[to_fill_id]
            rows[i] += 1
            if rows[i] == m:
                return k
            cols[j] += 1
            if cols[j] == m:
                return k
