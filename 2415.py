from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        bfs_queue = deque()
        bfs_queue.append(root)
        depth = 0
        while bfs_queue:
            n = len(bfs_queue)
            if n == 0:
                break
            print(n)
            for _ in range(n):
                cur_node = bfs_queue.popleft()
                if not cur_node or not cur_node.left:
                    continue
                bfs_queue.append(cur_node.left)
                bfs_queue.append(cur_node.right)
            if depth % 2 == 0:
                node_l = list(bfs_queue)
                reversed_vals = list(reversed(list(map(lambda x: x.val, node_l))))
                for i in range(len(node_l)):
                    node_l[i].val = reversed_vals[i]
                print("done")
            depth += 1
        return root
