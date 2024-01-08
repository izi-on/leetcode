# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        if subRoot is None:
            return True

        if root is None:
            return False

        def dfs(root, subRoot):
            if subRoot is None:
                return True if root is None else False
            if root is None:
                return True if subRoot is None else False
            l = dfs(root.left, subRoot.left)
            r = dfs(root.right, subRoot.right)
            if l and r and root.val == subRoot.val:
                return True
            return False

        if dfs(root, subRoot):
            return True

        if self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot):
            return True

        return False
