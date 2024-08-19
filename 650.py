class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        i = 1
        cp = 0
        moves = 0
        while i < n:
            if n % i == 0:
                cp = i
                i += cp
                moves += 2
            else:
                i += cp
                moves += 1
        return moves
