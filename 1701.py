from collections import deque


class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        cur_time = 0
        total_wait_time = 0
        for customer in customers:
            extra_wait = max(0, cur_time - customer[0])
            total_wait_time += extra_wait + customer[1]
            cur_time = max(cur_time + customer[1], customer[0] + customer[1])
        return total_wait_time / len(customers)
