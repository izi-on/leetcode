from math import log, floor


class Solution:
    def kthCharacter(self, k: int) -> str:
        cur = k - 1
        dc = 0
        while cur:
            dc += 1
            to_remove = 1 << floor(log(cur))
            cur = cur - to_remove
        return ascii((ord("a") + dc) % 26)
