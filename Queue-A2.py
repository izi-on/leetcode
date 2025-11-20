class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0
        req = tickets[k]
        for i in range(len(tickets)):
            if i <= k:
                time += min(tickets[i], req)
            else:
                time += min(tickets[i], req - 1)
        return time
