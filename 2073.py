class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        return sum(list(map(lambda x: min(x, tickets[k]), tickets)))
