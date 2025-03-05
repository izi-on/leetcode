class Solution:
    def coloredCells(self, n: int) -> int:
        return 1 + n * (n - 1) * 4 // 2
