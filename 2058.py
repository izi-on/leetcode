# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        idx = 1
        crit_idx = []
        prevNode = head
        cur_node = head.next
        while cur_node and cur_node.next:
            if (prevNode.val - cur_node.val) * (cur_node.next.val - cur_node.val) > 0:
                crit_idx.append(idx)
            idx += 1
            prevNode = cur_node
            cur_node = cur_node.next
        if len(crit_idx) < 2:
            return [-1, -1]
        minDistance = float("infinity")
        for i in range(1, len(crit_idx)):
            minDistance = min(minDistance, crit_idx[i] - crit_idx[i - 1])
        return [minDistance, crit_idx[-1] - crit_idx[0]]
