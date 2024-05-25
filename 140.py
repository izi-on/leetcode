class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        answer = []
        word_set = set(wordDict)

        def helper(cur, s_idx):
            if s_idx == len(s):
                return
            for i in range(s_idx, len(s)):
                cur_word = s[s_idx : i + 1]
                if cur_word in word_set:
                    cur.append(cur_word)
                    if i == len(s) - 1:
                        answer.append(" ".join(cur.copy()))
                    helper(cur, i + 1)
                    cur.pop()

        helper([], 0)
        return answer
