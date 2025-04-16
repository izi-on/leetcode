from collections import defaultdict


class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        right = 0
        freq_count = defaultdict(int)
        ans = 0
        cur_count = 0
        for left in range(n):
            while right < n and cur_count < k:
                cur_count += freq_count[nums[right]]
                freq_count[nums[right]] += 1
                right += 1
            if cur_count >= k:
                # print(freq_count, right)
                ans += n - right + 1
                cur_count -= freq_count[nums[left]] - 1
                freq_count[nums[left]] -= 1
        return ans
