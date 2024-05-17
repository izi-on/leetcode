# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(
        self, root: Optional[TreeNode], target: int
    ) -> Optional[TreeNode]:
        def helper(root):
            if not root:
                return False
            if helper(root.left):
                root.left = None
            if helper(root.right):
                root.right = None
            if not root.left and not root.right and root.val == target:
                return True
            return False

        if helper(root):
            return None
        return root
