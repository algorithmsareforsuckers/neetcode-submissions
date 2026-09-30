# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        beg = ListNode(0, ListNode())
        curr = beg
        prev = beg


        while l1 or l2 or carry:
            curr.next = ListNode()
            curr = curr.next

            p1 = l1.val if l1 else 0
            p2 = l2.val if l2 else 0
            val = p1 + p2 + carry
            carry = 1 if val >= 10 else 0
            val = val % 10

            curr.val = val 
            prev = curr
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return beg.next