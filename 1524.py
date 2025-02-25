class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        dp = [[_ for _ in range(2)] for _ in range(len(arr) + 1)]
        dp[0][0] = 0
        dp[0][1] = 0
        for i in range(1, len(arr) + 1):
            idx = i - 1
            cur = arr[idx]
            if cur % 2 == 1:
                dp[i][0] = dp[i - 1][1] + 1  # + 1 by itself
                dp[i][1] = dp[i - 1][0]
            else:
                dp[i][0] = dp[i - 1][0]
                dp[i][1] = dp[i - 1][1] + 1
        return sum(list(map(lambda x: x[0], dp)))
