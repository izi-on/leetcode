# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        bfs = deque()
        if root:
            bfs.append(root)
        ans = []
        while bfs:
            n = len(bfs)
            for i in range(n):
                node = bfs.popleft()
                if i == 0:
                    ans.append(node.val)
                if node.right:
                    bfs.append(node.right)
                if node.left:
                    bfs.append(node.left)
        return ans
