from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.is_valid = True

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not self.is_valid:
                return (0, 0)

            if root is None:
                return (float("infinity"), -float("infinity"))

            res_left = dfs(root.left)
            res_right = dfs(root.right)
            if not (res_left[1] < root.val < res_right[0]):
                self.is_valid = False
                return (0, 0)
            return (min(res_left[0], root.val), max(root.val, res_right[1]))

        dfs(root)
        return self.is_valid
