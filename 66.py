class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]
        carry = 1
        for i in range(len(digits)):
            digits[i] = (digits[i] + carry) % 10
            carry = int(digits[i] == 0 and carry)
        digits += [1] * carry
        return digits[::-1]
