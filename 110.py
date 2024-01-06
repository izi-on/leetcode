# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        def dfs(root):
            if root is None:
                return (True, 0)
            b_l, h_l = dfs(root.left)
            b_r, h_r = dfs(root.right)
            if not b_l or not b_r:
                return (False, -1)
            if abs(h_l - h_r) > 1:
                return (False, -1)
            return (True, max(h_l + 1, h_r + 1))

        return dfs(root)[0]
