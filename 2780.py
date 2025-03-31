from collections import defaultdict
import heapq


class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        count_l, count_r = defaultdict(int), defaultdict(int)
        for num in nums:
            count_r[num] + 1

        for i in range(len(nums) - 1):
            num = nums[i]
            count_l[num] += 1
            count_r[num] -= 1
            if (
                count_l[num] > (i + 1) // 2
                and count_r[num] > (len(nums) - (i + 1)) // 2
            ):
                return i

        return -1
