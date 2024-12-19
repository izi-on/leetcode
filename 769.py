from functools import reduce
from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        s_arr = sorted(arr)
        num_to_idx = reduce(lambda acc, v: {**acc, v[1]: v[0]}, enumerate(s_arr), {})
        intervals = []
        for i in range(len(arr)):
            num = arr[i]
            mn, mx = min(i, num_to_idx[num]), max(i, num_to_idx[num])
            intervals.append([mn, mx])
        intervals.sort()
        count_component = 1
        max_end = intervals[0][1]
        for i in range(1, len(intervals)):
            if max_end < intervals[i][0]:
                count_component += 1
            max_end = max(max_end, intervals[i][1])
        return count_component
