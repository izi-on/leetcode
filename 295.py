import heapq


class MedianFinder:
    def __init__(self):
        self.left_max = []
        self.right_min = []

    def addNum(self, num: int) -> None:
        largest_left = -self.left_max[0] if self.left_max else -float("infinity")
        if num > largest_left:
            heapq.heappush(self.right_min, num)
        else:
            heapq.heappush(self.left_max, -num)
        larger = (
            self.left_max
            if len(self.left_max) > len(self.right_min)
            else self.right_min
        )
        smaller = (
            self.left_max
            if len(self.left_max) <= len(self.right_min)
            else self.right_min
        )
        if len(larger) - len(smaller) > 1:
            balance = heapq.heappop(larger)
            heapq.heappush(smaller, -balance)

    def findMedian(self) -> float:
        total = len(self.left_max) + len(self.right_min)
        if total % 2 == 0:
            return (-self.left_max[0] + self.right_min[0]) / 2
        else:
            if len(self.left_max) > len(self.right_min):
                return -self.left_max[0]
            else:
                return self.right_min[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
