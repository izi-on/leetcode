class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        right = -1
        c0 = 0
        ans = 0
        for left in range(n):
            while right < n and c0 < 2:
                ans = max(ans, right - left)
                # print("considering", nums[left: right + 1])
                right += 1
                c0 += 1 if right < n and nums[right] == 0 else 0
            c0 -= 1 if nums[left] == 0 else 0
        return ans
