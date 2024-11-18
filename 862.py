import heapq


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        prefix_sum = []
        cur_sum = 0
        for num in nums:
            cur_sum += num
            prefix_sum.append(cur_sum)

        prefix_heap = [(0, -1)]
        ans = float("inf")
        for i, prefix in enumerate(prefix_sum):
            heapq.heappush(prefix_heap, (prefix, i))
            while prefix - prefix_heap[0][0] >= k:
                ans = min(ans, i - heapq.heappop(prefix_heap)[1])
        return ans if ans != float("inf") else -1

