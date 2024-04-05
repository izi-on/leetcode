class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        cur = n
        while cur >= 2:
            if cur in visited:
                return False
            new_num = 0
            while cur != 0:
                new_num += (cur % 10) ^ 2
                cur //= 10
            cur = new_num
            visited.add(cur)
        return cur == 1
