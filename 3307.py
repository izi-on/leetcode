class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        cur = k - 1
        dc = 0
        while cur:
            op = cur.bit_length() - 1
            if operations[op] == 1:
                dc += 1
            to_remove = 2 ** floor(log2(cur))
            cur = cur - to_remove
        return chr(ord("a") + (dc % 26))
