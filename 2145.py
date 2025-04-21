class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        start = 0
        track_max = 0
        track_min = 0
        for diff in differences:
            start += diff
            track_max = max(track_max, start)
            track_min = min(track_min, start)
        gap = track_max - track_min
        gap_info = upper - lower
        return gap_info - gap + 1 if gap_info >= gap else 0
