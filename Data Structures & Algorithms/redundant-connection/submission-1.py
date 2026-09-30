class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)

        for v,w in edges:
            adj[v].append(w)
            adj[w].append(v)

        visited = set()
        cycle_start = -1
        cycle = set()
        def dfs(w, v):
            nonlocal cycle_start

            if w in visited:
                cycle_start = w
                return True
            
            visited.add(w)
            for nei in adj[w]:
                if nei == v: continue
            
                if dfs(nei, w):
                    if cycle_start != -1:
                        cycle.add(w)
                    if w == cycle_start:
                        cycle_start = -1
                    return True
            return False

            
        
        dfs(1,-1)

        for v,w in reversed(edges):
            if v in cycle and w in cycle: 
                return [v,w]
        
        return []
            