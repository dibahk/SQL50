# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeZeroSumSublists(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        org = ListNode(0, head)
        start = org
        while start is not None:
            sum = 0
            end = start.next
            while end is not None:
                sum += end.val
                if sum == 0:
                    start.next = end.next
                end = end.next
            start = start.next

        return org.next
