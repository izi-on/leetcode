import heapq


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1
        bloomed = set()
        p = [i for i in range(len(bloomDay))]
        r = [1 for _ in range(len(bloomDay))]

        def parent(i):
            nonlocal p
            if p[i] != i:
                p[i] = parent(p[i])
            return p[i]

        def union(a, b):
            p_a = parent(a)
            p_b = parent(b)
            if r[p_a] > r[p_b]:
                p[p_b] = p_a
                r[p_a] += r[p_b]
                return r[p_a]
            else:
                p[p_a] = p_b
                r[p_b] += r[p_a]
                return r[p_b]

        heap = []
        bouquets = 0
        for i, bd in enumerate(bloomDay):
            heapq.heappush(heap, (bd, i))
        while heap:
            bd, i = heapq.heappop(heap)
            bloomed.add(i)
            count = 2
            if i - 1 in bloomed and i + 1 in bloomed:
                l = r[parent(i - 1)]
                r_ = r[parent(i + 1)]
                union(i - 1, i)
                union(i, i + 1)
                if (l % k) + (r_ % k) + 1 >= k:
                    count = k
            elif i - 1 in bloomed:
                count = union(i - 1, i)
            elif i + 1 in bloomed:
                count = union(i + 1, i)

            if count % k == 0:
                bouquets += 1
            if bouquets == m:
                return bd
        return -1
