import heapq
from collections import defaultdict, deque


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        pq = []
        queue = deque()
        task_count = defaultdict(int)
        for task in tasks:
            task_count[task] += 1
        for _, count in task_count.items():
            heapq.heappush(pq, -count)

        t = 0
        while pq or queue:
            if len(queue) > 0 and queue[0][1] <= t:
                new = queue.popleft()
                heapq.heappush(pq, new[0])
            if pq:
                cur = heapq.heappop(pq)
                if cur != -1:
                    queue.append((cur + 1, t + n + 1))
            t += 1
        return t
