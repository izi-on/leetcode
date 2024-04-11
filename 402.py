class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        def adjust(answer: str):
            while answer and answer[0] == "0":
                answer = answer[1:]
            if not answer:
                return "0"
            return answer

        stack = []
        for n in num:
            while stack and stack[-1] > n and k > 0:
                stack.pop()
                k -= 1
            stack.append(n)
        while k > 0:
            stack.pop()
            k -= 1
        return adjust("".join(list(stack)))


# class Solution:
#     def removeKdigits(self, num: str, k: int) -> str:
#
#         def dfs(prefix: str, k: int):
#             if len(prefix) <= k:
#                 return ""
#             if k == 0:
#                 return prefix
#             idx_min = -1
#             min_val = float("inf")
#             for i, c in enumerate(prefix[: k + 1]):
#                 num = int(c)
#                 if num < min_val:
#                     idx_min = i
#                     min_val = num
#             return prefix[idx_min] + dfs(prefix[idx_min + 1 :], k - idx_min)
#
#         return adjust(dfs(str(num), k))
