from typing import List


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        answer = 0

        def helper(node):
            nonlocal answer
            if node is None:
                return []
            if node.left is None and node.right is None:
                return [0]
            else:
                ln_l = helper(node.left)
                ln_r = helper(node.right)
                ln_l = [l + 1 for l in ln_l if l < distance]
                ln_r = [r + 1 for r in ln_r if r < distance]
                for l in ln_l:
                    for r in ln_r:
                        if l + r <= distance:
                            answer += 1
                return ln_l + ln_r

        helper(root)
        return answer
