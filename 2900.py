class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        dp = [[1, 0]] if groups[0] == 0 else [[0, 1]]
        for i in range(1, n):
            if groups[i] == 1:
                cur_max = max(dp[-1][0] + 1, dp[-1][1])
                dp.append([dp[-1][0], cur_max])
            else:
                cur_max = max(dp[-1][1] + 1, dp[-1][0])
                dp.append([cur_max, dp[-1][1]])
        ans = []
        cur_group = -1
        for i in range(len(dp) - 1, -1, -1):
            if dp[i][0] >= dp[i][1] and cur_group != 0:  # group 0 better and compatible
                ans.append(words[i])
                cur_group = 0
            elif dp[i][1] >= dp[i][0] and cur_group != 1:
                ans.append(words[i])
                cur_group = 1
        return reversed(ans)
