# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def helper(root, left):
            if not root:
                return 0
            if not root.left and not root.right:
                return root.val if left else 0
            sum = helper(root.left, True)
            sum += helper(root.right, False)
            return sum

        return helper(root, False)
