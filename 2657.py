class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        num_a, num_b = set(), set()
        c = []
        for i in range(n):
            num_a.add(A[i])
            num_b.add(B[i])
            nums = num_a.intersection(num_b)
            c.append(len(nums))
        return c
