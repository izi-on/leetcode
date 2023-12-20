import heapq
from collections import deque


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        # init the window
        deq = deque()

        # init the deque
        for num in nums[:k]:
            while deq[0] < num:
                deq.popleft()
            deq.append(num)

        answer = []
        for num in range(nums[k:]):


