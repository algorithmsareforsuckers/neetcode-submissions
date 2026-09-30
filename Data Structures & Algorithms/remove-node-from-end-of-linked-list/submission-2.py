# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head
        length = 0
        curr = head

        while curr:
            length += 1
            curr = curr.next
        
        remove = length - n + 1
        beg = ListNode(0, head)
        curr = beg

        for _ in range(remove - 1):
            curr = curr.next
        curr.next = curr.next.next

        return beg.next
        