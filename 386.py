from collections import deque


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        answer = []

        def helper(cur_num):
            nonlocal answer
            if cur_num > n:
                return
            answer.append(cur_num)
            # option 1: extend current number
            helper(cur_num * 10)

            # option 2: increment the current number
            if cur_num % 10 != 9:
                helper(cur_num + 1)

        helper(1)
        return answer
