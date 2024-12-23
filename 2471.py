from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        bfs = deque()
        bfs.append(root)
        count = 0
        while bfs:
            n = len(bfs)
            for _ in range(n):
                cur_node = bfs.popleft()
                if not cur_node:
                    continue
                if cur_node.left:
                    bfs.append(cur_node.left)
                if cur_node.right:
                    bfs.append(cur_node.right)

            ll = list(map(lambda x: x.val, bfs))
            target = sorted(ll)
            pos = {val: i for i, val in enumerate(ll)}
            for i in range(len(ll)):
                if ll[i] != target[i]:
                    new_val_idx = pos[target[i]]
                    ll[i], ll[new_val_idx] = ll[new_val_idx], ll[i]
                    pos[ll[new_val_idx]] = new_val_idx

                    count += 1
        return count
