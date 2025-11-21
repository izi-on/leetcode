from collections import defaultdict
from functools import cmp_to_key


class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda i: (i[1], -i[0]))
        last_added = [-1, -1]
        count = 0
        for i in range(len(intervals)):
            s, e = intervals[i]
            if last_added[1] < s:
                last_added = [e - 1, e]
                count += 2
            elif last_added[0] < s:
                last_added = [last_added[1], e]
                count += 1
        return count
