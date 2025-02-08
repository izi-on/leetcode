import heapq
from collections import defaultdict


class NumberContainers:
    def __init__(self):
        self.idx_to_num = {}
        self.num_to_idx = defaultdict(list)

    def change(self, index: int, number: int) -> None:
        self.idx_to_num[index] = number
        heapq.heappush(self.num_to_idx[number], index)

    def find(self, number: int) -> int:
        if number not in self.num_to_idx.keys() or not self.num_to_idx[number]:
            return -1
        while number != self.idx_to_num[self.num_to_idx[number][0]]:
            heapq.heappop(self.num_to_idx[number])
            if not self.num_to_idx[number]:
                return -1
        if not self.num_to_idx:
            return -1
        return self.num_to_idx[number][0]


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)

