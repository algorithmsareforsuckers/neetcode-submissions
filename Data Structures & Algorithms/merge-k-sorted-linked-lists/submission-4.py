# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minheap = []
        #val_list = {}
        for i, node in enumerate(lists):
            if node and node.val is not None: 
                #val_list[(node.val,i)] = node
                heapq.heappush(minheap, (node.val,i, node))
        
        head = ListNode()
        prev = head
        while minheap:
            mn,i, mn_node = heapq.heappop(minheap)
            #mn_node = val_list[(mn,i)]
            prev.next = mn_node

            if mn_node.next: 
                heapq.heappush(minheap, (mn_node.next.val,i,mn_node.next))
                #val_list[(mn_node.next.val,i)] = mn_node.next
            prev = mn_node
        
        return head.next
            


