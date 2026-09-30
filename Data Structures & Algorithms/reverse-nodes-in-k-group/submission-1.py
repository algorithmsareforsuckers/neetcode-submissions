# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return head

        beg = ListNode(next=head)
        curr = beg # On first iter, we set curr = dummy, where 
                   # dummy = curr.next, so we will start at head
        tail = curr

        while curr:
            i = 0
            check = curr
            while check and i < k:
                check = check.next
                i += 1
            
            if i != k or not check: break
            dummy = curr.next
            tail = check.next
            group_before = curr
            group_first = curr.next


            # Confirmed there are at least k elements left
            for _ in range(k):
                curr = dummy
                dummy = curr.next # on final element is None
                curr.next = tail
                tail = curr

            group_before.next = curr
            curr = group_first # curr.next is the start of the next group
            
            #dummy2 = iter_start.next
            #iter_start.next = curr
            #curr = dummy2
            #curr.next = dummy
        return beg.next
