# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pointer1 = head
        pointer2 = head
        while pointer2 is not None and pointer2.next is not None:
            pointer1 = pointer1.next
            pointer2 = pointer2.next.next
        return pointer1
