class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        chars = set()
        longest = 0
        ptr_b = 0
        for i, c in enumerate(s):
            while c in chars:
                chars.remove(s[ptr_b])
                ptr_b += 1
                continue
            chars.add(c)
            longest = max(longest, i-ptr_b+1)
        return longest


        