# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def constructFromPrePost(
        self, preorder: List[int], postorder: List[int]
    ) -> Optional[TreeNode]:
        n = len(preorder)
        preorder_val_to_idx = {}
        postorder_val_to_idx = {}
        for i in range(n):
            preorder_val = preorder[i]
            postorder_val = postorder[i]
            preorder_val_to_idx[preorder_val] = i
            postorder_val_to_idx[postorder_val] = i

        def helper(cur_sub_preorder, cur_sub_postorder):
            nonlocal preorder, postorder
            start_preorder_idx, end_preorder_idx = cur_sub_preorder
            start_postorder_idx, end_postorder_idx = cur_sub_postorder
            n = end_preorder_idx - start_preorder_idx
            if n < 0:
                return None
            if n == 0:
                return TreeNode(preorder[start_preorder_idx])
            if n == 1:
                node = TreeNode(preorder[start_preorder_idx])
                node.left = TreeNode(preorder[start_preorder_idx + 1])
                return node
            root_val = preorder[start_preorder_idx]
            node = TreeNode(root_val)
            left_val = preorder[start_preorder_idx + 1]
            right_val = postorder[end_postorder_idx - 1]
            left_sub_tree = helper(
                (start_preorder_idx + 1, preorder_val_to_idx[right_val] - 1),
                (start_postorder_idx, postorder_val_to_idx[left_val]),
            )
            right_sub_tree = helper(
                (preorder_val_to_idx[right_val], end_preorder_idx),
                (postorder_val_to_idx[left_val] + 1, end_postorder_idx - 1),
            )
            node.left = left_sub_tree
            node.right = right_sub_tree
            return node

        return helper((0, len(preorder) - 1), (0, len(postorder) - 1))
