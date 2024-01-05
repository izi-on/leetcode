# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    diameter = 0

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.helper(root)
        return self.diameter

    def helper(self, root):
        if root is None:
            return 0
        l_h = self.helper(root.left)
        r_h = self.helper(root.right)
        self.diameter = max(self.diameter, l_h + r_h)
        return max(l_h + 1, r_h + 1)
