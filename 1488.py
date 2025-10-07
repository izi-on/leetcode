class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        point_to_next_occurence = [float("inf") for _ in range(n)]
        prev_day = {}
        for i in range(n - 1, -1, -1):
            rainy_lake = rains[i]
            if rainy_lake in prev_day.keys():
                point_to_next_occurence[i] = prev_day[rainy_lake]
            prev_day[rainy_lake] = i

        ans = [-1 for _ in range(n)]
        heap = []
        full_lakes = set()
        for i in range(n):
            rainy_lake = rains[i]
            if rainy_lake == 0:
                _, lake_to_clear = heapq.heappop(heap) if heap else (None, None)
                if lake_to_clear:
                    ans[i] = lake_to_clear
                    full_lakes.remove(lake_to_clear)
                else:
                    ans[i] = 1
            else:
                if rainy_lake in full_lakes:
                    return []
                full_lakes.add(rainy_lake)
                heapq.heappush(heap, (point_to_next_occurence[i], rainy_lake))
        return ans
