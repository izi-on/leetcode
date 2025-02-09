from collections import defaultdict


class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        # j - i = nums[j] - nums[i]
        # => j - nums[j] = i - nums[i]
        n = len(nums)
        freq_count = defaultdict(int)
        total = 0
        for i in range(n):
            cur_val = i - nums[i]
            total += freq_count[cur_val]
            freq_count[cur_val] += 1
        return n * (n - 1) // 2 - total
