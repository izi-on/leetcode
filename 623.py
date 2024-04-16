# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(
        self, root: Optional[TreeNode], val: int, depth: int
    ) -> Optional[TreeNode]:
        if depth == 1:
            new_node = TreeNode(val, root)
            new_node.left = root
            return new_node

        def helper(depth, cur, parent, left):
            if depth == 1:
                if left:
                    new_node = TreeNode(val, cur)
                    parent.left = new_node
                    return
                else:
                    new_node = TreeNode(val, None, cur)
                    parent.right = new_node
                    return
            if cur is None:
                return
            helper(depth - 1, cur.left, cur, True)
            helper(depth - 1, cur.right, cur, False)

        helper(depth - 1, root.left, root, True)
        helper(depth - 1, root.right, root, False)
        return root
