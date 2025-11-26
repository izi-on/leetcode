import heapq


class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        n = len(apples)
        heap = []  # (days, amt)
        ans = 0
        for i in range(n):
            if apples[i] == 0 and days[i] == 0:
                pass
            else:
                heapq.heappush(heap, (i + days[i], apples[i]))

            while heap and heap[0][0] <= i:
                heapq.heappop(heap)
            if heap:
                d, amt = heapq.heappop(heap)
                amt -= 1
                ans += 1
                if amt:
                    heapq.heappush(heap, (d, amt))
        i = n
        print("heap", heap)
        while heap:
            while heap and heap[0][0] <= i:
                heapq.heappop(heap)
            if not heap:
                break
            d, amt = heapq.heappop(heap)
            to_rem = min(d - i, amt)
            i += to_rem
            print(to_rem)
            ans += to_rem

        return ans
