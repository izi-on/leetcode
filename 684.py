class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        p_list: list = [i for i in range(n + 1)]
        rank: list = [1 for _ in range(n + 1)]

        def parent(i):
            nonlocal p_list
            if p_list[i] == i:
                return i
            p_list[i] = parent(p_list[i])
            return p_list[i]

        def union(a, b):
            nonlocal p_list
            nonlocal rank
            p_a = parent(a)
            p_b = parent(b)
            if p_a == p_b:
                return
            if rank[p_a] > rank[p_b]:
                p_list[p_b] = p_a
            elif rank[p_b] < rank[p_a]:
                p_list[p_a] = p_b
            else:
                p_list[p_a] = p_b
                rank[p_b] += 1

        redundant = None
        for edge in edges:
            a, b = edge
            parent_a = parent(a)
            parent_b = parent(b)
            if parent_a == parent_b:
                redundant = edge
                continue
            union(a, b)
        return redundant
