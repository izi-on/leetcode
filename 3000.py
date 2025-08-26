class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        return list(
            reversed(sorted([(x[0] ** 2 + x[1] ** 2, x[0] * x[1]) for x in dimensions]))
        )[0][1]
