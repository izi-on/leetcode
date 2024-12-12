import math
from functools import reduce
import heapq


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gft = list(map(lambda x: (-x[1], x[0]), enumerate(gifts)))
        gft_track = reduce(lambda p, n: {**p, n[1]: -n[0]}, gft, {})
        # print(gft_track)
        heapq.heapify(gft)
        for _ in range(k):
            gft_amt, id = heapq.heappop(gft)
            gft_amt = -gft_amt
            # print(gft_track[id], gft_amt, gft_track[id] != -gft_amt)
            while gft_track[id] != gft_amt:
                # print("----")
                # print("removing", gft_amt, id)
                # print(gft_track)
                # print("----")
                gft_amt, id = heapq.heappop(gft)
                gft_amt = -gft_amt
            # print("passed")
            # print("----")
            # print("adding", gft_amt, id)
            # print("----")
            gft_track[id] = math.floor(math.sqrt(gft_amt))
            heapq.heappush(gft, (-gft_track[id], id))
        return sum(gft_track.values())
