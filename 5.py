class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_length = 0
        ans = None
        for i in range(len(s)):
            # odd
            ptr_l, ptr_r = i, i
            length = -1
            while 0 <= ptr_l and ptr_r < len(s):
                if s[ptr_l] != s[ptr_r]:
                    break
                ptr_l -= 1
                ptr_r += 1
                length += 2
            ptr_l += 1
            ptr_r -= 1
            # print("odd", s[ptr_l: ptr_r+1], (ptr_l, ptr_r))
            if length > max_length:
                ans = s[ptr_l : ptr_r + 1]
                max_length = length

            if i == len(s) - 1:
                break

            # even
            ptr_l, ptr_r = i, i + 1
            length = 0
            while 0 <= ptr_l and ptr_r < len(s):
                if s[ptr_l] != s[ptr_r]:
                    break
                ptr_l -= 1
                ptr_r += 1
                length += 2
            ptr_l += 1
            ptr_r -= 1
            if length > max_length:
                ans = s[ptr_l : ptr_r + 1]
                max_length = length

        return ans
