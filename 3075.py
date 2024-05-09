import heapq


class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness = list(map(lambda x: -x, happiness))
        heapq.heapify(happiness)
        turn = 0
        sum = 0
        while len(happiness) and -happiness[0] - turn > 0 and turn < k:
            sum += -heapq.heappop(happiness) - turn
            turn += 1
        return sum
