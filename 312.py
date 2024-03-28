class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        dp = {}
        nums = [1] + nums + [1]

        def dfs(i, j):
            if j - i == 0:
                return 0
            if (i, j) in dp:
                return dp[(i, j)]
            max_val = 0
            for k in range(i, j):
                print(nums[i:j], "popping", k - i)
                increment_val = nums[i - 1] * nums[k] * nums[j]
                max_val = max(dfs(i, k) + dfs(k + 1, j) + increment_val, max_val)
                print(nums[i:j], "max_val", max_val)
            dp[(i, j)] = max_val
            return max_val

        return dfs(1, len(nums) - 1)
