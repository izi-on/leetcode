class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        self.root = root

    def find(self, target: int) -> bool:
        dfs_stack = [(self.root, 0)]
        while dfs_stack:
            cur = dfs_stack.pop()
            node, val = cur
            if node is None:
                continue
            if val == target:
                return True
            cur.val = val
            dfs_stack.append((node.right, 2 * val + 2))
            dfs_stack.append((node.left, 2 * val + 1))
        return False
