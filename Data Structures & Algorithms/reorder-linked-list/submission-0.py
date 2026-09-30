# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return None

        # 1. Find middle of list and seperate 1st half, 2nd half
        p1 = head
        p2 = head.next

        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
        sh = p1.next
        p1.next = None

        # 2. Reverse second half
        prev = None

        while sh:
            curr = sh
            sh = sh.next
            curr.next = prev
            prev = curr

        # 3. Interweave
        r = prev
        l = head

        while r:
            nl = l.next
            nr = r.next

            l.next = r
            l.next.next = nl

            r = nr
            l = nl
        
        return None
            