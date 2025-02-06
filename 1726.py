from collections import defaultdict


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        n = len(nums)
        product_freq = defaultdict(int)
        for i in range(n):
            for j in range(i + 1, n):
                prod = nums[i] * nums[j]
                product_freq[prod] += 1
        total = 0
        for val in product_freq.values():
            total += ((val) * (val - 1) // 2) * (8)
        return total
