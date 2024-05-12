import heapq


class Solution:
    def mincostToHireWorkers(
        self, quality: List[int], wage: List[int], k: int
    ) -> float:
        # sort based on wage to quality ratio
        wage_to_quality = [
            (wage[i] / quality[i], quality[i]) for i in range(len(quality))
        ]
        wage_to_quality = sorted(wage_to_quality)

        # create priority queue to track highest quality
        highest_quality = []

        # keep track of total quality
        total_quality = 0

        # keep track of min cost
        min_cost = float("infinity")

        for i in range(len(wage_to_quality)):
            heapq.heappush(highest_quality, -wage_to_quality[i][1])
            total_quality += wage_to_quality[i][1]

            if len(highest_quality) > k:
                quality = -heapq.heappop(highest_quality)
                total_quality -= quality

            if len(highest_quality) == k:
                min_cost = min(min_cost, total_quality * wage_to_quality[i][0])
        return min_cost
