import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        heapq.heapify(heap)
        for point in points:
            i, j = point
            heapq.heappush(heap, (-(i**2) - j**2, i, j))
        while len(heap) > k:
            heapq.heappop(heap)
        return list(map(lambda x: [x[1], x[2]], heap))
