# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def helper(cur: TreeNode | None, pass_val):
            if cur is None:
                return 0
            r = helper(cur.right, pass_val)
            l = helper(cur.left, r + cur.val + pass_val)
            old_val = cur.val
            cur.val = r + pass_val + old_val
            return r + l + old_val

        helper(root, 0)
        return root
