import heapq


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals = sorted(intervals)
        queries = list(map(lambda x: [x[1], x[0]], enumerate(queries)))
        queries = sorted(queries)
        min_heap = []
        interval_ptr = 0
        ans = [-1 for _ in queries]
        for query, id in queries:
            while interval_ptr < len(intervals) and intervals[interval_ptr][1] < query:
                interval_ptr += 1
            while interval_ptr < len(intervals) and intervals[interval_ptr][0] <= query:
                heapq.heappush(
                    min_heap,
                    [
                        intervals[interval_ptr][1] - intervals[interval_ptr][0] + 1,
                        intervals[interval_ptr][1],
                    ],
                )
                interval_ptr += 1
            while min_heap and not (
                min_heap[0][1] - min_heap[0][0] + 1 <= query <= min_heap[0][1]
            ):
                heapq.heappop(min_heap)
            if min_heap:
                ans[id] = min_heap[0][0]
        return ans
