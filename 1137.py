class Solution:
    def tribonacci(self, n: int) -> int:
        mem = [-1] * 38
        mem[0] = 0
        mem[1] = 1
        mem[2] = 1
        for i in range(3, n + 1):
            mem[i] = mem[i - 1] + mem[i - 2] + mem[i - 3]
        return mem[n]
