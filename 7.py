class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        is_negative = False
        if x < 0:
            is_negative = True
            x *= -1
        while x != 0:
            rev *= 10
            to_add = x % 10
            if x > (2**31 - 1 - to_add) // 10:
                return 0
            rev += to_add
            x //= 10
        return rev if is_negative == False else -rev
