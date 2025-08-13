class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        baskets = sorted(baskets)
        used = set()
        placed = 0
        for f in fruits:
            cand = -1
            for i, b in enumerate(baskets):
                if i in used:
                    continue
                if b < f:
                    continue
                cand = i
                break
            if cand != -1:
                used.add(cand)
                placed += 1
        return len(fruits) - placed
