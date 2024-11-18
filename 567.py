from collections import defaultdict


class Solution(object):
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2):
            return False
        char_count_s1 = defaultdict(int)
        for c in s1:
            char_count_s1[c] += 1

        # init interval
        char_count = defaultdict(int)

        def check_equal():
            for c, count in char_count_s1.items():
                if char_count[c] != count:
                    return False
            return True

        for i in range(len(s1)):
            char_count[s2[i]] += 1
        if check_equal():
            return True

        for i in range(len(s1), len(s2)):
            char_count[s2[i]] += 1
            char_count[s2[i - len(s1)]] -= 1
            if check_equal():
                return True
        return False
