from collections import defaultdict, deque


class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        answer = 0

        def helper(root):
            nonlocal answer
            if root is None:
                return 0
            balance_l = helper(root.left)
            balance_r = helper(root.right)
            total_balance = balance_l + balance_r + root.val - 1
            answer += abs(total_balance)
            return total_balance

        helper(root)
        return answer
