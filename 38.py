class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        start = ["1"]
        for _ in range(1, n):
            new_start = []
            count_cur = 0
            cur_num = start[0]
            for num in start:
                if num != cur_num:
                    new_start.append(str(count_cur))
                    new_start.append(cur_num)
                    count_cur = 1
                    cur_num = num
                else:
                    count_cur += 1
            if count_cur:
                new_start.append(str(count_cur))
                new_start.append(cur_num)
            start = new_start
        return "".join(start)
