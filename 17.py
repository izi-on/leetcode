class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dig_to_let = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        answer = []

        def dfs(idx, cur):
            if idx == len(digits):
                answer.append("".join(cur))
                return
            cur_digit = digits[idx]
            for letter in dig_to_let[cur_digit]:
                cur.append(letter)
                dfs(idx + 1, cur)
                cur.pop()

        if not digits:
            return []
        dfs(0, [])
        return answer
