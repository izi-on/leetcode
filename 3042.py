class TrieNode:
    def __init__(self, val=None):
        self.val = val
        self.children = {}
        self.is_end = set()


class Solution:
    def get_prefixes(self, root: TrieNode, word):
        cur = root
        ans = set()
        for c in word:
            if c not in cur.children.keys():
                return ans
            cur = cur.children[c]
            ans.update(cur.is_end)
        return ans

    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        # build trie prefixes
        root = TrieNode()
        for i, word in enumerate(words):
            cur = root
            for c in word:
                if c not in cur.children.keys():
                    new_node = TrieNode(c)
                    cur.children[c] = new_node
                cur = cur.children[c]
            cur.is_end.add(i)

        # build tree suffixes
        root_rev = TrieNode()
        for i, word in enumerate(words):
            cur = root_rev
            for c in word[::-1]:
                if c not in cur.children.keys():
                    new_node = TrieNode(c)
                    cur.children[c] = new_node
                cur = cur.children[c]
            cur.is_end.add(i)

        total = 0
        for i, word in enumerate(words):
            word_prefixes = self.get_prefixes(root, word)
            word_suffixes = self.get_prefixes(root_rev, word[::-1])
            match = word_prefixes.intersection(word_suffixes)
            total += len(list(filter(lambda x: x < i, match)))
        return total
