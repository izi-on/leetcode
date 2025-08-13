import heapq
from collections import Counter, defaultdict, deque


class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        freq = defaultdict(int)
        m = float("inf")
        for b in basket1:
            freq[b] += 1
            m = min(m, b)
        for b in basket2:
            freq[b] -= 1
            m = min(m, b)

        to_merge = []
        for b, c in freq.items():
            if c % 2 == 1:
                return -1
            to_merge.extend([b] * (c // 2))

        return sum(min(x, 2 * m) for x in sorted(to_merge)[: len(to_merge) // 2])
