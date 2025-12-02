from collections import defaultdict


class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MOD = 10**9 + 7
        group_h = defaultdict(list)
        for p in points:
            x, y = p
            group_h[y].append((x, y))

        gs = group_h.items()
        count_poss = 0
        ans = 0
        for g in gs:
            _, points = g
            amt = len(points) * (len(points) - 1) // 2
            ans = (ans + (amt * count_poss)) % MOD
            count_poss = (count_poss + amt) % MOD
        return ans
