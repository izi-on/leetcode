import heapq


class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        r_max = len(arr) - k - 1
        min_heap = []
        for i in range(r_max, len(arr)):
            for j in range(i):
                heapq.heappush(min_heap, (arr[j] / arr[i], arr[j], arr[i]))
        k -= 1
        while k != 0:
            k -= 1
            heapq.heappop(min_heap)
        return heapq.heappop(min_heap)[1:]
