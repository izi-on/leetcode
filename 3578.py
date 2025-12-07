import heapq
from collections import defaultdict
from typing import List


def get_max(heap, counter):
    while heap and counter[-heap[0]] == 0:
        heapq.heappop(heap)
    return -heap[0]


def get_min(heap, counter):
    while heap and counter[heap[0]] == 0:
        heapq.heappop(heap)
    return heap[0]


MOD = 10**9 + 7


class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0] * n
        prefix = [0] * (n + 1)
        min_heap_window = []
        max_heap_window = []
        num_count = defaultdict(int)

        tail = 0
        dp[0] = 1
        prefix[1] = 1

        heapq.heappush(min_heap_window, nums[0])
        heapq.heappush(max_heap_window, -nums[0])
        num_count[nums[0]] += 1

        for i in range(1, n):
            num = nums[i]
            heapq.heappush(min_heap_window, num)
            heapq.heappush(max_heap_window, -num)
            num_count[num] += 1

            mx = get_max(max_heap_window, num_count)
            mn = get_min(min_heap_window, num_count)
            while tail <= i and mx - mn > k:
                num_count[nums[tail]] -= 1
                tail += 1
                mx = get_max(max_heap_window, num_count)
                mn = get_min(min_heap_window, num_count)

            if tail == 0:
                dp[i] = (1 + prefix[i]) % MOD
            else:
                dp[i] = (prefix[i] - prefix[tail - 1]) % MOD

            prefix[i + 1] = (prefix[i] + dp[i]) % MOD

        return dp[-1]
