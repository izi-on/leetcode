class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        n = len(hats)
        hat_to_people = [[] for _ in range(41)]
        for i, _hats in enumerate(hats):
            for h in _hats:
                hat_to_people[h].append(i)

        MOD = 10**9 + 7

        mem = {}

        def topdown(hat, bitmask):
            if hat == 0:
                if bitmask == 2**n - 1:
                    return 1
                else:
                    return 0
            if (hat, bitmask) in mem:
                return mem[(hat, bitmask)]
            # option 1: skip
            # topdown(hat - 1, bitmask)
            # option 2: assign hat
            # all possible
            # topdown(hat - 1, n_bitmask)
            skip_poss = topdown(hat - 1, bitmask)
            ans = 0
            for person in hat_to_people[hat]:
                if bitmask & (1 << person) > 0:
                    continue
                n_bitmask = bitmask | 1 << person
                ans += topdown(hat - 1, n_bitmask)
            mem[(hat, bitmask)] = (skip_poss + ans) % MOD
            return mem[(hat, bitmask)]

        return topdown(40, 0)
