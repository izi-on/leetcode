import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = list(map(lambda x: -1 * x, stones))
        heapq.heapify(stones)
        while len(stones) > 1:
            stone1 = -1 * heapq.heappop(stones)
            stone2 = -1 * heapq.heappop(stones)
            remainder = abs(stone1 - stone2)
            if not remainder == 0:
                heapq.heappush(stones, -1 * remainder)
        return -1 * stones[0]
