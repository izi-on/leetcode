class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        ptr = 0
        answer = []
        intervals = (
            [[-float("infinity"), -float("infinity")]]
            + intervals
            + [[float("infinity"), float("infinity")]]
        )

        # find first potential intersection
        while newInterval[0] < intervals[ptr][1]:
            answer.append(intervals[ptr])
            ptr += 1

        newInterval[0] = min(newInterval[0], intervals[ptr][0])

        while newInterval[1] >= intervals[ptr][0]:
            newInterval[1] = max(intervals[ptr][1], newInterval[1])
            ptr += 1

        answer.append(newInterval)
        answer += intervals[ptr:]

        return answer[1:-1]
