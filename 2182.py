import heapq
from functools import reduce


class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        track = reduce(lambda acc, v: {**acc, v: acc.get(v, 0) + 1}, list(s), {})
        pq = list(
            map(
                lambda x: (
                    -ord(x[0]),
                    x[0],
                    x[1],
                ),
                track.items(),
            )
        )
        heapq.heapify(pq)
        repetition = 0
        repeated = "*"
        ans = []
        while pq:
            r, c, amt = heapq.heappop(pq)
            if repeated == c:
                if repetition == repeatLimit:
                    if not pq:
                        return "".join(ans)
                    r_new, c_new, amt_new = heapq.heappop(pq)
                    heapq.heappush(pq, (r, c, amt))
                    r, c, amt = r_new, c_new, amt_new
            if repeated != c:
                repeated = c
                repetition = 0
            repetition += 1
            ans.append(c)
            amt -= 1
            if amt != 0:
                heapq.heappush(pq, (r, c, amt))
        return "".join(ans)
