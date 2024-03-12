import heapq


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        p = [i for i in range(len(points))]
        r = [0 for _ in points]

        def find(i):
            if i == p[i]:
                return i
            p[i] = find(p[i])
            return p[i]

        def union(a, b):
            p_a = find(a)
            p_b = find(b)
            if r[p_a] > r[p_b]:
                p[p_b] = p_a
                r[p_a] += 1
            else:
                p[p_a] = p_b
                r[p_b] += 1

        edges = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                distance = abs(points[i][0] - points[j][0]) + abs(
                    points[i][1] - points[j][1]
                )
                edges.append([distance, (i, j)])

        heapq.heapify(edges)
        cost = 0
        while len(edges) > 0:
            distance, (i, j) = heapq.heappop(edges)
            if find(i) == find(j):
                continue
            union(i, j)
            cost += distance
        return cost
