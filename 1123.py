from collections import deque


class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        bfs = deque([(root, None)])
        deepest = []
        prev = {}
        while bfs:
            n = len(bfs)
            deepest.clear()
            for _ in range(n):
                cur_node, parent = bfs.popleft()
                prev[cur_node] = parent
                deepest.append(cur_node)
                if cur_node.left:
                    bfs.append((cur_node.left, cur_node))
                if cur_node.right:
                    bfs.append((cur_node.right, cur_node))
        to_backtrack = set(deepest)
        while len(to_backtrack) > 1:
            new_backtrack = set()
            for node in to_backtrack:
                new_backtrack.add(prev[node])
            to_backtrack = new_backtrack
        return next(iter(to_backtrack))
