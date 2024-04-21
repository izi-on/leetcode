class Solution:
    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        p = [i for i in range(n)]
        r = [0] * n

        def get_p(a):
            if p[a] == a:
                return a
            p[a] = get_p(p[a])
            return p[a]

        def union(a, b):
            p_a = get_p(a)
            p_b = get_p(b)
            if p_a == p_b:
                return
            if r[p_a] < r[p_b]:
                p[p_a] = p_b
                r[p_b] += 1
            else:
                p[p_b] = p_a
                r[p_a] += 3

        for edge in edges:
            union(edge[0], edge[1])

        return get_p(source) == get_p(destination)
