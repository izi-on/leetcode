class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals)
        to_compare = intervals[0]
        ans = 0
        for interval in intervals[1:]:
            if to_compare[1] > interval[0]:
                if to_compare[1] > interval[1]:
                    to_compare = interval
                ans += 1
        return ans
