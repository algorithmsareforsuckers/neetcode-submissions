# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # needed 2 hints
        if not head:
            return False
        p1 = head
        p2 = head
        parity = 1

        while p2.next:
            p2 = p2.next
            if p1 == p2:
                return True
            if parity:
                p1 = p1.next
            parity  = (parity + 1)%2

        return False

