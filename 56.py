class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        cur_interval = None
        answer = [intervals[0]]
        for i in range(1, len(intervals)):
            prev_interval = answer[-1]
            cur_interval = intervals[i]
            if cur_interval[0] <= prev_interval[1]:
                prev_interval[1] = max(cur_interval[1], prev_interval[1])
            else:
                answer.append(cur_interval)
        return answer
