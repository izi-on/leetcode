from functools import reduce
import bisect


class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        s = sum(apple)
        ps_s_cap = reduce(
            lambda acc, x: acc + [acc[-1] + x], sorted(capacity, reverse=True), [0]
        )[1:]
        return bisect.bisect_left(ps_s_cap, s) + 1
