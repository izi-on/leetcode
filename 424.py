from collections import defaultdict
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        track_diff = defaultdict(int)
        ptr = 0
        cur_max = 0
        longest = 0
        for i,c in enumerate(s):
            track_diff[c] += 1
            cur_max = max(track_diff[c], cur_max)
            if k < (i - ptr + 1) - cur_max:
                track_diff[s[ptr]] -= 1
                ptr += 1
                cur_max = max(track_diff.values())
            longest = max(i - ptr + 1, longest)
        return longest