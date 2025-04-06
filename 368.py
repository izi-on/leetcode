class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)
        # if nums[i] % nums[i - 1] == 0 and nums[i + 1] % nums[i] == 0, then nums[i+1] % nums[i-1] == 0 TRIVIAL, skill issue if you can't figure this out
        dp = [1]  # first index: not included, second index: included
        prev_dp = {0: 0}
        for i in range(1, len(nums)):
            num = nums[i]
            dp.append(1)
            prev_dp[i] = i
            for j in range(i):
                if num % nums[j] == 0:
                    if dp[i] < dp[j] + 1:
                        dp[i] = dp[j] + 1
                        prev_dp[i] = j
        # print(dp)
        start = max(map(lambda x: x[::-1], enumerate(dp)))[1]

        # backtrack and find solution
        ans = []
        cur = start
        while cur != prev_dp[cur]:
            ans.append(nums[cur])
            cur = prev_dp[cur]
        ans.append(nums[cur])
        return ans[::-1]
