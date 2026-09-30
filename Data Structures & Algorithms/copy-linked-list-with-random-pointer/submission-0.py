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
        copy = Node(0)
        beg = copy

        h = head
        inds = {}
        n = 0
        while h:
            copy.next = Node(h.val, None, None)

            copy = copy.next
            h = h.next

            inds[n] = copy
            n += 1

        h, n = head, 0
        while h:
            h.val = n
            n += 1
            h = h.next

        copy, h = beg.next, head
        while copy:
            if not h.random:
                h = h.next
                copy = copy.next
                continue
            
            copy.random = inds[h.random.val]
            h = h.next
            copy = copy.next
        
        return beg.next

            
