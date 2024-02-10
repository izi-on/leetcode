import heapq
from collections import defaultdict, deque
from types import TracebackType


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        groupAmt = len(hand) // groupSize
        track_request = defaultdict(list)
        count_completed = 0
        hand = sorted(hand)
        for h in hand:
            requests = track_request[h]
            if not requests:
                track_request[h + 1].append(0)
                requests = track_request[h + 1]
            requests[-1] += 1
            if requests[-1] == groupSize:
                count_completed += 1
                requests.pop()
            else:
                cur = requests.pop()
                track_request[h + 1].append(cur)
        return count_completed == groupAmt
