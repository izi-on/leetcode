class Solution:
    def find_sum(self, num, target, cur_sum):
        if num == 0:
            return cur_sum == target
        cur_num = 0
        found = False
        while num != 0:
            cur_num = cur_num * 10 + (num % 10)
            if self.find_sum(num // 10, target, cur_num + cur_sum):
                found = True
        return found

    def punishmentNumber(self, n: int) -> int:
        for i in range(n):
            num = i**2
            if self.find_sum(num, i, 0):
                return i
        return -1
