class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        t = []
        vowels = set(["a", "e", "u", "i", "o"])
        count = 0
        for word in words:
            if word[-1] in vowels and word[0] in vowels:
                count += 1
            t.append(count)
        ans = []
        for query in queries:
            prev = t[query[0] - 1] if query[0] > 0 else 0
            ans.append(t[query[1]] - prev)
        return ans
