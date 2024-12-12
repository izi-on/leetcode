from collections import deque


class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        intervals = map(lambda x: [x - k, x + k], nums)
        intervals = sorted(intervals, key=lambda x: x[1])
        ans = 0
        overlapping_stack = deque()
        for interval in intervals:
            overlapping_stack.append(interval)
            while not overlapping_stack[0][0] <= interval[0] <= overlapping_stack[0][1]:
                overlapping_stack.popleft()
            ans = max(len(overlapping_stack), ans)
        return ans
