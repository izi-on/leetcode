from functools import reduce


class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)
        res = 0
        if m % 2 == 1:
            res = reduce(lambda acc, v: acc ^ v, nums1, res)
        if n % 2 == 1:
            res = reduce(lambda acc, v: acc ^ v, nums2, res)
        return res
