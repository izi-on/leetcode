class Solution:
    def minOperations(self, nums: List[int]) -> int:
        stack = []
        ans = 0
        for i in range(len(nums)):
            num = nums[i]
            while stack and stack[-1] > num:
                ans += 1
            stack.append(num)
        return ans + len(stack)
