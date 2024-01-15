# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = -float("infinity")

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if root is None:
                return 0

            get_left_max = dfs(root.left)
            get_right_max = dfs(root.right)
            self.ans = max(self.ans, get_left_max + get_right_max + root.val, root.val)
            return max(get_left_max + root.val, get_right_max + root.val, 0)

        dfs(root)
        return self.ans
