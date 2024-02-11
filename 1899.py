import heapq


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        passes = [0 for _ in range(3)]
        for triplet in triplets:
            for i in range(3):
                if target[i] == triplet[i] and not [
                    1 for i in range(3) if target[i] < triplet[i]
                ]:
                    passes[i] = 1
        return sum(passes) == 3
