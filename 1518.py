import math


class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        answer = 0
        fullBottles = numBottles
        emptyBottles = 0
        while fullBottles:
            answer += fullBottles
            emptyBottles += fullBottles
            fullBottles = emptyBottles // numExchange
            emptyBottles = emptyBottles % numExchange
        return answer
