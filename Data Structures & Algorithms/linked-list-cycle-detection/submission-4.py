# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        fast = head.next
        slow = head

        while fast and fast.next and fast != slow:
            fast = fast.next.next
            slow = slow.next
        
        if not fast or not fast.next:
            return False

        return True
        

        # met at some node C_k
        p3 = head
        n = 0
        while p3 != slow:
            p3 = p3.next
            slow = slow.next
            n += 1
        
        return True