# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        ptr1 = list1
        ptr2 = list2
        new_list = ListNode()
        new_head = new_list

        while ptr1 and ptr2:
            if ptr1.val < ptr2.val:
                new_list.next = ptr1
                ptr1 = ptr1.next
            else:
                new_list.next = ptr2
                ptr2 = ptr2.next
            new_list = new_list.next

        while ptr1:
            new_list.next = ptr1
            new_list = new_list.next
            ptr1 = ptr1.next

        while ptr2:
            new_list.next = ptr2
            new_list = new_list.next
            ptr2 = ptr2.next

        return new_head.next
