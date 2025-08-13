class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        n = len(parent)

        class TrieNode:
            def __init__(self, value):
                self.value = value
                self.children = []

            def add_child(self, node):
                self.children.append(node)

        new_parents = parent.copy()
        roots = [0]
        for i, p in enumerate(parent):
            if s[i] == s[p]:
                roots.append(i)
                new_parents[i] = -1
        parent = new_parents

        nodes = [TrieNode(i) for i, _ in enumerate(parent)]

        for i, p in enumerate(parent):
            if p == -1:
                continue
            nodes[p].add_child(nodes[i])

        longest = 0

        def longest_finder(cur_node):
            nonlocal longest
            if cur_node is None:
                return 0

            two_longest = [0, 0]
            for child in cur_node.children:
                candidate = longest_finder(child)
                if candidate > two_longest[0]:
                    two_longest = [candidate, two_longest[0]]
                elif candidate > two_longest[1]:
                    two_longest = [two_longest[0], candidate]

            longest = max(longest, two_longest[0] + two_longest[1] + 1)
            return two_longest[0] + 1

        for r in roots:
            longest_finder(nodes[r])

        return longest
