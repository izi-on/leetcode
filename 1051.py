from functools import reduce


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        return reduce(
            lambda x, y: x + 1 if y[0] != y[1] else x,
            list(zip(*[[*heights], [*sorted(heights)]])),
            0,
        )
