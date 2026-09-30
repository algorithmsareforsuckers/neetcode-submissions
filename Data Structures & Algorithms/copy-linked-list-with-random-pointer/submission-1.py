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
        beg = Node(0)
        inds = {}

        copy, h, n = beg, head, 0
        while h:
            copy.next = Node(h.val, None, None)
            h.val = n
            inds[n] = copy.next

            copy, h, n = copy.next, h.next, n+1

        copy, h = beg.next, head
        while copy:
            if h.random:
                copy.random = inds[h.random.val]
            h, copy = h.next, copy.next
        
        return beg.next

            
