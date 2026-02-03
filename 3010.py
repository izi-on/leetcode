import heapq


class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        heap = []
        for n in nums[1:]:
            heapq.heappush(heap, n)
        s = nums[0]
        c = 2
        while c and len(heap):
            s += heapq.heappop(heap)
            c -= 1
        return s
