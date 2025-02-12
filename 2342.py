from collections import defaultdict
import heapq


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def sum_digits(num):
            s = 0
            while num:
                dig = num % 10
                s += dig
                num //= 10
            return s

        dig_sum = list(map(sum_digits, nums))
        freq_count = defaultdict(list)
        for i in range(len(dig_sum)):
            s = dig_sum[i]
            heapq.heappush(freq_count[s], -nums[i])
        max_s = -1
        for _, v in freq_count.items():
            if len(v) > 1:
                max_s = max(max_s, -heapq.heappop(v) + -heapq.heappop(v))
        return max_s

