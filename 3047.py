class Solution:
    def largestSquareArea(
        self, bottomLeft: List[List[int]], topRight: List[List[int]]
    ) -> int:
        n = len(bottomLeft)
        tmax = 0
        for i in range(n):
            for j in range(i + 1, n):
                bl1 = bottomLeft[i]
                tr1 = topRight[i]

                bl2 = bottomLeft[j]
                tr2 = topRight[j]

                if (
                    tr2[0] <= bl1[0]
                    or tr1[0] <= bl2[0]
                    or tr1[1] <= bl2[1]
                    or tr2[1] <= bl1[1]
                ):
                    continue

                bl_int_x = max(bl1[0], bl2[0])
                bl_int_y = max(bl1[1], bl2[1])

                tr_int_x = min(tr1[0], tr2[0])
                tr_int_y = min(tr1[1], tr2[1])

                max_sqr = min(tr_int_y - bl_int_y, tr_int_x - bl_int_x) ** 2
                tmax = max(tmax, max_sqr)
        return tmax
