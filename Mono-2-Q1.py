class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        stack = []  # (num, idx)
        ans = 0
        for i in range(len(nums)):
            num = nums[i]
            while stack and stack[-1][0] > num:
                _, pidx = stack.pop()
                ans += i - pidx
            stack.append((num, i))
        i = len(nums)
        while stack:
            _, pidx = stack.pop()
            ans += i - pidx
        return ans
