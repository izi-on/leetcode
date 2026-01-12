import math


class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def get_div(num):
            divs = []
            for i in (1, num**0.5 + 1):
                if num % i == 0:
                    divs.append(i)
                    if num // i != i:
                        divs.append(num // i)
            return divs

        return sum([sum(get_div(n)) for n in nums if len(get_div(n)) == 4])
