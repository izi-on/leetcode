from collections import defaultdict
from functools import reduce


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(s) < len(t):
            return ""

        # Input: s = "ADOBECODEBANC", t = "ABC"
        # Output: "BANC"

        t_dict = defaultdict(int)

        def make(x, y):
            x[y] += 1
            return x

        reduce(lambda x, y: make(x, y), t, t_dict)
        ptr_e = 0
        ptr_s = 0
        track_smallest = float("infinity")
        track_s_e = -1
        track_s_s = -1

        def check_dicts():
            for k in t_dict.keys():
                if s_dict[k] < t_dict[k]:
                    return False
            return True

        s_dict = defaultdict(int)
        while ptr_e < len(s):
            cur_char = s[ptr_e]
            s_dict[cur_char] += 1
            while check_dicts():
                (track_s_s, track_s_e) = (
                    (ptr_s, ptr_e)
                    if track_smallest > ptr_e - ptr_s + 1
                    else (track_s_s, track_s_e)
                )
                track_smallest = min(track_smallest, ptr_e - ptr_s + 1)
                s_dict[s[ptr_s]] -= 1
                ptr_s += 1
            ptr_e += 1
        return s[track_s_s : track_s_e + 1]
