from collections import defaultdict


class Solution:
    def findAllPeople(
        self, n: int, meetings: List[List[int]], firstPerson: int
    ) -> List[int]:
        tm = defaultdict(list)
        for m in meetings:
            tm[m[2]].append((m[0], m[1]))
        meetings = sorted(tm.items())
        hs = [False] * n
        hs[0] = True
        hs[firstPerson] = True

        def find(p, i):
            if p[i] == i:
                return i
            p[i] = find(p, p[i])
            return p[i]

        def union(p, r, a, b):
            pa = find(p, a)
            pb = find(p, b)
            if hs[pa] or hs[pb]:
                hs[pa] = True
                hs[pb] = True
            if pa == pb:
                return
            if r[pa] < r[pb]:
                p[pa] = pb
                r[pb] += r[pa]
            else:
                p[pb] = pa
                r[pa] += r[pb]

        for meeting in meetings:
            gs = meeting[1]
            p = {}
            r = {}
            candidates = set()
            for m in gs:
                p1, p2 = m
                candidates.add(p1)
                candidates.add(p2)
                for pc in [p1, p2]:
                    if pc not in p:
                        p[pc] = pc
                        r[pc] = 1
                union(p, r, p1, p2)

            for c in candidates:
                pc = find(p, c)
                if hs[pc]:
                    hs[c] = True

        return [i for i in range(n) if hs[i]]
