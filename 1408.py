from typing import Set


class TrieNode:
    def __init__(self, val=None):
        self.val = val
        self.children = {}
        self.is_end = False


class Solution:
    def get_subs(self, root: TrieNode, word) -> Set:
        subs = set()
        for i in range(len(word)):
            cword = word[i:]
            cur = root
            bword = []
            for c in cword:
                if c not in cur.children.keys():
                    break
                bword.append(c)
                cur = cur.children[c]
                if cur.is_end:
                    subs.add("".join(bword))
        return subs

    def stringMatching(self, words: List[str]) -> List[str]:
        # build trie
        root = TrieNode()
        for word in words:
            cur = root
            for c in word:
                if c not in cur.children:
                    new_node = TrieNode(c)
                    cur.children[c] = new_node
                cur = cur.children[c]
            cur.is_end = True

        # check substring
        ans = set()
        for word in words:
            subs = self.get_subs(root, word) - set([word])
            print(subs)
            ans.update(subs)

        return list(ans)
