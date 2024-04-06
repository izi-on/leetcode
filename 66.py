class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        remainder = 0
        def increment(ptr):
            nonlocal remainder
            digits[ptr] = (digits[ptr] + 1) % 10
            if digits[ptr] == 0:
                remainder = 1
            else:
                remainder = 0
        ptr = len(digits)-1
        increment(ptr)
        while remainder and ptr > 0:
            ptr -= 1
            increment(ptr)
        if ptr == 0 and remainder:
            digits = [1] + digits
        return digits
            
            
        