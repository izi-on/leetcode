"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals = list(map(lambda x: [x.start, x.end], intervals))
        intervals = sorted(intervals)
        for i in range(1, len(intervals)):
            if intervals[i - 1][1] > intervals[i][0]:
                return False
        return True
