class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        new_inters = []
        for inter in intervals:
            s, e = inter
            if not new_inters:
                new_inters.append([s, e])
            elif new_inters and new_inters[-1][1] < s:
                new_inters.append([s, e])
            else:
                new_inters[-1][1] = max(new_inters[-1][1], e)
        return new_inters
