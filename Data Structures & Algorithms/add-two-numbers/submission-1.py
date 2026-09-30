# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        h1 = l1
        h2 = l2
        while h1 and h2:
            add = h1.val + h2.val + carry
            if add - 10 >= 0:
                carry = 1
                add = add % 10
            else:
                carry = 0
            
            h1.val = add

            prev1 = h1
            prev2 = h2
            h1, h2 = h1.next, h2.next

        end = None
        if h1:
            end = h1
        elif h2:
            prev1.next = h2
            end = prev1.next
        
        # might still have h2 vals left
        while end and carry:
            if end.val == 9:
                end.val = 0
            else:
                carry = 0
                end.val += 1

            prev1 = end
            end = end.next
        
        if carry == 1:
            prev1.next = ListNode(1)
        

        return l1
        
            