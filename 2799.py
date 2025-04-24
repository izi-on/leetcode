from collections import Counter


class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        def get_all_nums(d: dict):
            nums = set()
            for k, v in d.items():
                if v != 0:
                    nums.add(k)
            return nums

        n = len(nums)
        unique_nums = set(nums)

        cur_freq_count = Counter()

        tail = 0
        ans = 0
        for i in range(n):
            cur_freq_count[nums[i]] += 1
            while tail <= i and get_all_nums(cur_freq_count) == unique_nums:
                ans += n - i
                cur_freq_count[nums[tail]] -= 1
                tail += 1
        return ans
