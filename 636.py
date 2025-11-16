from collections import defaultdict


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        def parse(log):
            id, _type, time = log.split(":")
            return int(id), _type, int(time)

        stack = []
        track_time = defaultdict(int)
        prev_t = 0
        for log in logs:
            id, _type, time = parse(log)
            if stack:
                cur_id = stack[-1]
                track_time[cur_id] += (
                    time - prev_t if _type == "end" else time - prev_t - 1
                )

            if _type == "start":
                stack.append(id)
            elif _type == "end":
                stack.pop()
            prev_t = time if _type == "end" else time - 1

        return [x[1] for x in sorted(track_time.items())]
