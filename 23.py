import heapq


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        pq = []
        heapq.heapify(pq)
        for node in lists:
            if node:
                heapq.heappush(pq, (node.val, node))

        new_list = ListNode()
        new_head = new_list
        while pq:
            _, node = heapq.heappop(pq)
            new_list.next = node
            new_list = new_list.next
            if node.next:
                heapq.heappush(pq, (node.next.val, node.next))

        return new_head.next
