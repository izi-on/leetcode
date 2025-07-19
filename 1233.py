class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        class TrieNode:
            def __init__(self, val, is_end=False, children=None):
                self.val = val
                self.is_end = is_end
                self.children = {}

        root = TrieNode(None)
        for f in folder:
            cur = root
            for c in f.split("/"):
                if not c:
                    continue
                c = "/" + c
                if c not in cur.children:
                    cur.children[c] = TrieNode(c)
                cur = cur.children[c]
            cur.is_end = True

        ans = []

        def helper(cur, built):
            if cur is None:
                return

            to_pop = False
            if cur.val:
                built.append(cur.val)
                to_pop = True

            if cur.is_end:
                ans.append("".join(built))
                built.pop()
                return

            for c in cur.children.values():
                helper(c, built)

            if to_pop:
                built.pop()

        helper(root, [])

        return ans
