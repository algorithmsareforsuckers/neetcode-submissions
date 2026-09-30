# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        if not list1:
            return list2
        if not list2:
            return list1

        curr = res

        while list1 or list2:
            op1, op2 = 101, 101 #larger than is possible for Node.val
            if list1:
                op1 = list1.val
                print(f"op1 is {op1}")
            if list2:
                op2 = list2.val
                print(f"op2 is {op2}")

            if op1 < op2:
                val = op1
                list1 = list1.next
            else:
                val = op2
                list2 = list2.next

            curr.val = val
            if list1 or list2:
                curr.next = ListNode()
                curr = curr.next
        
        return res
