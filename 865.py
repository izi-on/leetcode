from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(node):
            if not node:
                return None, 0
            ln, ld = helper(node.left)
            rn, rd = helper(node.right)
            if ld == rd:
                return node, ld + 1
            elif ld < rd:
                return rn, rd + 1
            else:
                return ln, ld + 1

        return helper(root)[0]
