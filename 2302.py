class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        head = 0
        cur_sum = 0
        ans = 0
        for i in range(n):
            while head < n and cur_sum * (head - i) <= k:
                cur_sum += nums[head]
                head += 1
            ans += head - i
            cur_sum -= nums[i]
        return ans
