class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        smaller_squares = set()
        i = 0
        while i * i <= c:
            smaller_squares.add(i * i)
            i += 1
        for square in smaller_squares:
            if (c - square) in smaller_squares:
                return True
        return False
