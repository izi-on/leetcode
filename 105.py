# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder and not inorder:
            return None
        cur_root = TreeNode()
        cur_root.val = preorder[0]
        mid = inorder.index(preorder[0])
        cur_root.left = self.buildTree(preorder[1 : mid + 1], inorder[0:mid])
        cur_root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])
        return cur_root
