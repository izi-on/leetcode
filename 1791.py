from collections import defaultdict


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        visited = set()
        for edge in edges:
            if edge[0] in visited:
                return edge[0]
            if edge[1] in visited:
                return edge[1]
            visited.add(edge[1])
            visited.add(edge[2])
