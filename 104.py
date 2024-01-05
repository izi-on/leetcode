# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        bfs = deque()
        bfs.append(root)
        depth = 0
        while bfs:
            n = len(bfs)
            depth += 1
            for _ in range(n):
                cur = bfs.popleft()
                if cur.left:
                    bfs.append(cur.left)
                if cur.right:
                    bfs.append(cur.right)
        return depth
