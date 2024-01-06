# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p:
            return True if not q else False
        if not q:
            return True if not p else False
        if p.val != q.val:
            return False
        left = self.isSameTree(p.left, q.left)
        if not left:
            return False
        return self.isSameTree(p.right, q.right)
