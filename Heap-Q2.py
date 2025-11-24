import heapq


class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        n = len(nums)
        sums = [0] * 3
        for i in range(n):
            num = nums[i]
            sc = sums.copy()
            sc[(num + sums[0]) % 3] = max(sc[(num + sums[0]) % 3], num + sums[0])
            sc[(num + sums[1]) % 3] = max(sc[(num + sums[1]) % 3], num + sums[1])
            sc[(num + sums[2]) % 3] = max(sc[(num + sums[2]) % 3], num + sums[2])
            sums = sc
        return sums[0]
