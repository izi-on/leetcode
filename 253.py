"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start_points = list(map(lambda x: (x.start, "start"), intervals))
        end_points = list(map(lambda x: (x.end, "end"), intervals))
        points = sorted([*start_points, *end_points])
        track_max = 0
        cur = 0
        for point in points:
            if point[1] == "start":
                cur += 1
                track_max = max(track_max, cur)
            elif point[1] == "end":
                cur -= 1
        return track_max
