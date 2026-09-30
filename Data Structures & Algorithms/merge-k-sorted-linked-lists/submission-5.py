# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minheap = []
        for i, node in enumerate(lists):
            if node: 
                minheap.append((node.val,i,node))
        heapq.heapify(minheap)
        
        dummy = ListNode()
        tail = dummy
        while minheap:
            _, i, mn_node = heapq.heappop(minheap)
            tail.next = mn_node

            if mn_node.next: 
                heapq.heappush(minheap, (mn_node.next.val,i,mn_node.next))
            tail = mn_node
        
        return dummy.next
            


