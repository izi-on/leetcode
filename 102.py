from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        bfs_queue = deque()
        bfs_queue.append(root)
        ans = []
        while bfs_queue:
            n = len(bfs_queue)
            cur = []
            for _ in range(n):
                node = bfs_queue.popleft()
                if not node:
                    continue
                cur.append(node.val)
                bfs_queue.append(node.left)
                bfs_queue.append(node.right)
            if cur:
                ans.append(cur)
        return ans
