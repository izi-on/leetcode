from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        bfs = deque([root])
        lvl = 1
        t = -float("inf")
        ans = 1
        while bfs:
            n = len(bfs)
            s = 0
            for _ in range(n):
                node = bfs.popleft()
                s += node.val
                if node.left:
                    bfs.append(node.left)
                if node.right:
                    bfs.append(node.right)
            if s > t:
                ans = lvl
                t = s
            lvl += 1
        return ans
