from collections import defaultdict


class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        city = defaultdict(int)
        for road in roads:
            city[road[0]] += 1
            city[road[1]] += 1
        rs = []
        for k, v in city.items():
            rs.append((v, k))
        rs = sorted(rs, reverse=True)
        importance = 0
        for deg, city in rs:
            importance += deg * n
            n -= 1
        return importance
