import bisect


class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        m_track = [0]
        e_events = sorted(events, key=lambda x: x[1])
        for ev in e_events:
            m_track.append(max(m_track[-1], ev[2]))
        e_events = [ev[1] for ev in e_events]

        ans = 0
        for ev in events:
            idx = bisect.bisect_left(e_events, ev[0])
            ans = max(m_track[idx] + ev[2], ans)
        return ans
