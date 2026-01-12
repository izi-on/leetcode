class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        s = sum([sum([abs(x) for x in row]) for row in matrix])
        count_neg = sum([len([x for x in row if x < 0]) for row in matrix])
        if count_neg % 2:
            me = min(min([abs(x) for x in row]) for row in matrix)
            return s - 2 * me
        else:
            return s
