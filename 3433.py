from typing import List
from collections import deque
from functools import cmp_to_key


def compare(a, b):
    if int(a[1]) == int(b[1]):
        return -1 if a[0] > b[0] else 1
    return -1 if int(a[1]) < int(b[1]) else 1


class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        events = sorted(events, key=cmp_to_key(compare))
        offline_queue = deque()
        track_offline = set()
        mentions = [0] * numberOfUsers
        all_mentions = 0
        for event in events:
            timestamp = int(event[1])
            while offline_queue and offline_queue[0][0] <= timestamp:
                _, id = offline_queue.popleft()
                track_offline.remove(id)
            if event[0] == "OFFLINE":
                offline_queue.append((timestamp + 60, int(event[2])))
                track_offline.add(int(event[2]))
            else:
                mentions_str = event[2]
                if mentions_str == "ALL":
                    all_mentions += 1
                elif mentions_str == "HERE":
                    for i in range(numberOfUsers):
                        if i in track_offline:
                            continue
                        mentions[i] += 1
                else:
                    ids = mentions_str.split(" ")
                    for id in ids:
                        mentions[int(id[2:])] += 1
        return [m + all_mentions for m in mentions]
