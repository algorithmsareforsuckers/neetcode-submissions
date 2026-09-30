"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        mp = {}
        to_visit = deque([node])
        while to_visit:
            curr = to_visit.popleft()
            if curr in mp:
                continue
            if curr.neighbors: to_visit += curr.neighbors
            mp[curr] = Node(curr.val)

        
        for old_node, new_node in mp.items():
            for edge in old_node.neighbors:
                new_node.neighbors.append(mp[edge])
        

        return mp[node]
