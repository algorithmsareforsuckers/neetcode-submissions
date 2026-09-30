# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head
        beg = ListNode(0, head)

        l = beg
        r = beg

        for _ in range(n):
            r = r.next
        
        while r and r.next:
            r = r.next
            l = l.next
        
        l.next = l.next.next
        return beg.next