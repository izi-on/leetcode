import bisect
from typing import List


class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        ssquares = sorted(squares, key=lambda x: x[1])
        bis_ssquares = [x[1] for x in ssquares]
        esquares = sorted(squares, key=lambda x: x[1] + x[2])
        bis_esquares = [x[1] + x[2] for x in esquares]

        p_li_ssquares = [0]
        p_yli_ssquares = [0]
        for sq in ssquares:
            p_li_ssquares.append(p_li_ssquares[-1] + sq[2])
            p_yli_ssquares.append(p_yli_ssquares[-1] + sq[1] * sq[2])

        p_li_esquares = [0]
        p_yli_esquares = [0]
        for sq in esquares:
            p_li_esquares.append(p_li_esquares[-1] + sq[2])
            p_yli_esquares.append(p_yli_esquares[-1] + (sq[1] + sq[2]) * sq[2])

        # A_i = l_i * max(0, h - y_i) + l_i * max(0, h - (y_i + l_i))
        #
        # for explicitly above y_i:
        # total_sum += l_i * (h - y_i)
        # total_sum += l_i * h - l_i * y_i
        #
        # for explicitly above y_i + l_i
        # total_sum -= l_i * (h - (y_i + l_i))
        # total_sum -= l_i * h - l_i * (y_i + l_i)
        def get_area(h):
            idx = bisect.bisect_left(bis_ssquares, h)
            area = h * (p_li_ssquares[idx]) - p_yli_ssquares[idx]

            idx = bisect.bisect_left(bis_esquares, h)
            area -= h * p_li_esquares[idx] - p_yli_esquares[idx]

            return area

        l, r = 0, max([c[1] + c[2] for c in squares])
        total_area = sum([sq[2] ** 2 for sq in squares])
        while abs(l - r) > 2 * 10**-5:
            mid = (l + r) / 2
            ar = get_area(mid)
            if 2 * ar < total_area:
                l = mid
            else:
                r = mid

        return (l + r) / 2
