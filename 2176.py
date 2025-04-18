from collections import defaultdict


class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        freq_count = defaultdict(set)
        ans = 0
        for i, num in enumerate(nums):
            if i / k in freq_count[num]:
                ans += 1
            freq_count[num].add(i)
        return ans
