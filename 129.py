# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def helper(root):
            if not root:
                return []
            if not root.left and not root.right:
                return [str(root.val)]
            left_side = helper(root.left)
            right_side = helper(root.right)

            left_side = [str(root.val) + val for val in left_side]
            right_side = [str(root.val) + val for val in right_side]
            return left_side + right_side

        all_paths = helper(root)
        return sum([int(val) for val in all_paths])
