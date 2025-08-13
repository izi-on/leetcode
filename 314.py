# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         map_to_col = defaultdict(list)
#         def helper(root, col):
#             if not root:
#                 return
#             map_to_col[col].append(root.val)
#             helper(root.left, col - 1)
#             helper(root.right, col + 1)
#         helper(root, 0)
#         # min_key = min(map_to_col.keys())
#         cols = sorted(map_to_col.items())
#         cols = list(map(lambda x: x[1], cols))
#         return cols
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        map_to_col = defaultdict(list)
        bfs = deque([(root, 0)])
        while bfs:
            n = len(bfs)
            for _ in range(n):
                node, col = bfs.popleft()
                map_to_col[col].append(node.val)
                bfs.append((node.left, col - 1)) if node.left else None
                bfs.append((node.right, col + 1)) if node.right else None

        cols = sorted(map_to_col.items())
        return [col[1] for col in cols]
