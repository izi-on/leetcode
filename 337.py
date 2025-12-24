# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            if node is None:
                return 0, 0
            l_max, l_max_c = helper(node.left)
            r_max, r_max_c = helper(node.right)
            ans = max(l_max_c + node.val + r_max_c, l_max + r_max)
            return ans, l_max + r_max

        return helper(root)[0]
