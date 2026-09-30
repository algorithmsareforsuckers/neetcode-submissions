"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return node
        mp = {node:Node(node.val)}
        q = deque([node])
        while q:
            curr = q.popleft()
            for v in curr.neighbors:
                if v not in mp: 
                    mp[v] = Node(v.val)
                    q.append(v)
                mp[curr].neighbors.append(mp[v])
        
        return mp[node]