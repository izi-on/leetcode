class Solution:
    def reverseParentheses(self, s: str) -> str:
        def helper(cur_idx):
            cur_str = ""
            i = cur_idx
            while i < len(s):
                if s[i] == "(":
                    new_str, end_idx = helper(i + 1)
                    cur_str += new_str
                    i = end_idx
                elif s[i] == ")":
                    break
                else:
                    cur_str += s[i]
                i += 1
            # print("returning", cur_str[::-1])
            return cur_str[::-1], i

        i = 0
        answer = ""
        while i < len(s):
            if s[i] == "(":
                cur_str, end_idx = helper(i + 1)
                answer += cur_str
                i = end_idx
            else:
                answer += s[i]
            i += 1
        # print("returning", cur_str[::-1])
        return answer
