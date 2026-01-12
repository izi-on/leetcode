# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        mem = {}
        MOD = 10**9 + 7

        def s(node):
            if node is None:
                return 0
            if node in mem:
                return mem[node]
            ls = s(node.left) if node.left else 0
            rs = s(node.right) if node.right else 0
            mem[node] = ls + rs + node.val
            return mem[node]

        ts = s(root)

        ans = -1

        min_diff = float("inf")

        print(ts)

        def helper(node):
            nonlocal ans, min_diff
            if node.left:
                ls = s(node.left)
                if abs(2 * ls - ts) < min_diff:
                    ans = (ls * (ts - ls)) % MOD
                    min_diff = abs(2 * ls - ts)

            if node.right:
                rs = s(node.right)
                if abs(2 * rs - ts) < min_diff:
                    ans = (rs * (ts - rs)) % MOD
                    min_diff = abs(2 * rs - ts)

            if node.left:
                helper(node.left)
            if node.right:
                helper(node.right)

        helper(root)

        return ans
