class Trie:
    # def __repr__(self) -> str:
    #     return f"{str(self.val)}, {[neighbor.__repr__() for neighbor in self.neighbors.values()]}"

    def __init__(self, val=None, is_end=False):
        self.val = val
        self.is_end = is_end
        self.neighbors = {}


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # build trie
        root = Trie()
        for word in wordDict:
            cur = root
            for c in word:
                if c not in cur.neighbors.keys():
                    new_node = Trie(c)
                    cur.neighbors[c] = new_node
                cur = cur.neighbors[c]
            cur.is_end = True

        visited = [False for _ in s] + [False]

        def helper(i: int):
            nonlocal root
            nonlocal visited
            nonlocal s
            if i == len(s):
                return True
            if visited[i]:
                return False
            visited[i] = True
            cur = root
            for j in range(i, len(s)):
                c = s[j]
                if c not in cur.neighbors.keys():
                    break
                cur = cur.neighbors[c]
                if cur.is_end:
                    if helper(j + 1):
                        return True
            return False

        return helper(0)
