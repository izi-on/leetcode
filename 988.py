# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import runtime_checkable
import string


class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        letters = string.ascii_lowercase

        def dfs(node, cur_path) -> str:
            if not node:
                return "z"
            if not node.left and not node.right:
                return letters[node.val] + cur_path
            smallest_left_str = dfs(node.left, letters[node.val] + cur_path)
            smallest_right_str = dfs(node.right, letters[node.val] + cur_path)
            print(node.val, "l and r", smallest_left_str, smallest_right_str)
            smallest = (
                smallest_left_str
                if smallest_left_str < smallest_right_str
                else smallest_right_str
            )
            return smallest

        return dfs(root, "")
