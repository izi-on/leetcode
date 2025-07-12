from collections import defaultdict
import heapq


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings = sorted(meetings)
        ptr = 0
        ends = []
        rooms = [i for i in range(n)]
        heapq.heapify(rooms)
        track_room_count = defaultdict(int)
        cur_time = 0
        while ptr < len(meetings):
            if rooms and ends:
                if ends[0][0] <= meetings[ptr][0]:
                    end, room = heapq.heappop(ends)
                    heapq.heappush(rooms, room)
                    cur_time = end
                else:
                    start, i, iend = meetings[ptr][0], ptr, meetings[ptr][1]
                    cur_time = max(cur_time, start)
                    new_room = heapq.heappop(rooms)
                    track_room_count[new_room] += 1
                    heapq.heappush(ends, (cur_time + iend - start, new_room))
                    ptr += 1
            elif rooms and not ends:
                start, i, iend = meetings[ptr][0], ptr, meetings[ptr][1]
                cur_time = max(cur_time, start)
                new_room = heapq.heappop(rooms)
                track_room_count[new_room] += 1
                heapq.heappush(ends, (cur_time + iend - start, new_room))
                ptr += 1
            elif not rooms and ends:
                end, room = heapq.heappop(ends)
                heapq.heappush(rooms, room)
                cur_time = end

        # print(track_room_count)
        mink, maxv = float("inf"), -1
        for k, v in track_room_count.items():
            if v > maxv or (v == maxv and k < mink):
                maxv = v
                mink = k
        return mink
