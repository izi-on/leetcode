class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        parent = [i for i in range(n)]
        rank = [1 for _ in range(n)]
        components = n

        def get_parent(i):
            if i == parent[i]:
                return i
            parent[i] = get_parent(parent[i])
            return parent[i]

        def union(a, b):
            nonlocal components
            p_a = get_parent(a)
            p_b = get_parent(b)
            if p_a == p_b:
                return
            components -= 1
            if rank[p_a] > rank[p_b]:
                parent[p_b] = p_a
                rank[p_a] += 1
            else:
                parent[p_a] = p_b
                rank[p_b] += 1

        for edge in edges:
            if get_parent(edge[0]) == get_parent(edge[1]):
                return False
            union(edge[0], edge[1])
        return True if components == 1 else False
