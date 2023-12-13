from collections import defaultdict
import copy 
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False
        
        # count dict for s1
        d_count = defaultdict(int)
        for c in s1: d_count[c] += 1

        ptr_s = 0
        ptr_e = 0
        while ptr_s < len(s2):
            while ptr_e < len(s2) and d_count[s2[ptr_e]] > 0:
                d_count[s2[ptr_e]] -= 1
                ptr_e += 1
            if ptr_e - ptr_s == len(s1):
                return True
            # print("considering: ", s2[ptr_s: ptr_e+1])
            d_count[s2[ptr_s]] += 1 if ptr_s < ptr_e else 0
            ptr_s += 1
            ptr_e = max(ptr_s, ptr_e)
        return False