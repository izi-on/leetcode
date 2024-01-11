# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.count_good = 0

    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxVal):
            if node is None:
                return

            if node.val >= maxVal:
                self.count_good += 1
                maxVal = node.val

            dfs(node.right, maxVal)
            dfs(node.left, maxVal)

        dfs(root, root.val)
        return self.count_good
