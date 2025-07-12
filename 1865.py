import heapq
from collections import defaultdict


class FindSumPairs:
    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.nums2c = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        cur = self.nums2[index]
        self.nums2c[cur] -= 1
        self.nums2[index] += val
        self.nums2c[self.nums2[index]] += 1

    def count(self, tot: int) -> int:
        ans = 0
        for n in self.nums1:
            ans += self.nums2c[tot - n]
        return ans


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
