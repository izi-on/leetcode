# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque


class Solution(object):
    def __init__(self):
        self.ans = None

    def dfs(self, root, p, q) -> set[int]:
        if not root or self.ans:
            return set()

        left = self.dfs(root.left, p, q)
        right = self.dfs(root.right, p, q)
        so_far = left.union(right)
        if root == p:
            so_far.add(1)
        if root == q:
            so_far.add(2)
        if len(so_far) == 2 and not self.ans:
            self.ans = root
            return so_far

        return so_far

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        self.dfs(root, p, q)
        return self.ans
