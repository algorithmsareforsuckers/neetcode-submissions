# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return head.next
        # count len(list)
        curr = head
        m = 0
        while curr:
            curr = curr.next
            m += 1

        k = m - n
        print(k)
        curr = head
        prev = ListNode(None, head)
        beg = prev
        for _ in range(k):
            prev = curr
            curr = curr.next
        
        prev.next = curr.next

        return beg.next