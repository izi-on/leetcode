from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        bfs = deque()
        if root:
            bfs.append(root)
        ans = []
        while bfs:
            ans.append(max(list(map(lambda x: x.val, bfs))))
            n = len(bfs)
            for _ in range(n):
                cur = bfs.popleft()
                if not cur:
                    continue
                if cur.left:
                    bfs.append(cur.left)
                if cur.right:
                    bfs.append(cur.right)
        return ans
