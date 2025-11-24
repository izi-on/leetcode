import string
from collections import defaultdict
import bisect


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        chars = string.ascii_lowercase
        map_c_to_i = defaultdict(list)

        for i in range(len(s)):
            map_c_to_i[s[i]].append(i)

        count = 0
        for i in range(len(chars)):
            for j in range(len(chars)):
                fs = chars[i]
                snd = chars[j]
                fs_idxs = map_c_to_i[fs]
                snd_idxs = map_c_to_i[snd]
                if (not fs_idxs) or (not snd_idxs):
                    continue
                if not fs_idxs[-1] - fs_idxs[0] > 1:
                    continue
                idx_l = bisect.bisect_right(snd_idxs, fs_idxs[0])
                idx_r = bisect.bisect_left(snd_idxs, fs_idxs[-1])
                if idx_l == idx_r:
                    continue
                count += 1
        return count
