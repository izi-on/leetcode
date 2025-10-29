class Solution:
    def smallestNumber(self, n: int) -> int:
        larg = 0
        shifts = 0
        while n:
            rem = n % 2
            if rem:
                larg = rem << shifts
            n = n >> 1
            shifts += 1
        return (larg << 1) - 1
