from typing import List


class Solution:
    def _get_words(self, idx_t, idx_w, dp, char_freq, target):
        # word found
        if idx_t == len(target):
            return 1

        # no work
        if idx_w == len(dp[0]):
            return 0

        # dp
        if dp[idx_t][idx_w] != -1:
            return dp[idx_t][idx_w]

        option_1 = self._get_words(idx_t, idx_w + 1, dp, char_freq, target)
        option_2 = char_freq[idx_w][ord(target[idx_t]) - ord("a")] * self._get_words(
            idx_t + 1, idx_w + 1, dp, char_freq, target
        )
        dp[idx_t][idx_w] = (option_1 + option_2) % (10**9 + 7)
        return dp[idx_t][idx_w]

    def numWays(self, words: List[str], target: str) -> int:
        dp = [[-1] * len(words[0]) for _ in range(len(target))]
        char_freq = [[0] * 26 for _ in range(len(words[0]))]
        for i in range(len(words[0])):
            for j in range(len(words)):
                char_freq[i][ord(words[j][i]) - ord("a")] += 1
        return self._get_words(0, 0, dp, char_freq, target)
