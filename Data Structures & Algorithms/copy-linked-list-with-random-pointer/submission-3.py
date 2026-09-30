"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        to_copy = {}
        beg = Node(0, Node(0), Node(0))
        curr = beg.next

        ch = head
        i = 0
        while ch:
            curr.val = ch.val
            if ch.next:
                curr.next = Node(0)
            
            to_copy[i] = curr

            ch.val = i
            curr = curr.next
            ch = ch.next
            i += 1
        
        
        print("hi")
        ch = head
        curr = beg.next
        while ch:
            if not ch.random:
                curr.random = None
            else:
                curr.random = to_copy[ch.random.val]

            curr = curr.next
            ch = ch.next
        
        return beg.next
