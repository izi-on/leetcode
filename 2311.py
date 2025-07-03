class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        dp = [-1 for _ in range(len(s))]
        num_track = [0 for _ in range(len(s))]
        s = s[::-1]

        # init vals
        if int(s[0]) <= k:
            dp[0] = 1
            num_track[0] = int(s[0])
        else:
            return 0

        for i in range(1, len(s)):
            c = s[i]
            if c == "0":
                dp[i] = dp[i - 1]
                num_track[i] = num_track[i - 1]
                continue
            elif c == "1":
                # option 1: exclude it
                cur_max = dp[-1]
                cur_max_nt = num_track[-1]
                # option 2: include, and track from the max possible
                cur_val = 2**i
                cur_max_for_i = 0
                cur_max_for_i_nt = 0
                for j in range(i - 1, -1, -1):
                    if num_track[j] + cur_val <= k:
                        if cur_max_for_i < dp[j]:
                            cur_max_for_i = dp[j]
                            cur_max_for_i_nt = num_track[j]
                cur_max_for_i += 1
                cur_max_for_i_nt += cur_val

                if cur_max < cur_max_for_i:
                    cur_max = cur_max_for_i
                    cur_max_nt = cur_max_for_i_nt
                dp[i] = cur_max
                num_track[i] = cur_max_nt
        return dp[-1]
