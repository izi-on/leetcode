from collections import deque
import heapq


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        ptr = 0
        answer = 1
        maxs: list[tuple[int, int]] = [(-nums[0], 0)]
        mins: list[tuple[int, int]] = [(nums[0], 0)]
        removed = -1
        for i in range(1, len(nums)):
            heapq.heappush(maxs, (-nums[i], i))
            heapq.heappush(mins, (nums[i], i))
            while maxs[0][1] <= removed:
                heapq.heappop(maxs)
            cur_max, _ = maxs[0]
            cur_max = -cur_max
            while mins[0][1] <= removed:
                heapq.heappop(mins)
            cur_min, _ = mins[0]
            if cur_max - cur_min > limit:
                removed = ptr
                ptr += 1
                continue
            answer += 1
        return answer
