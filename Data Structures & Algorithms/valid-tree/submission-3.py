class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1: return False
        
        adj = [[] for _ in range(n)]
        for v,w in edges:
            adj[v].append(w)
            adj[w].append(v)

        visited = set()
        q = deque([(0,-1)])
        visited.add(0)

        while q:
            v, par = q.popleft()
            for w in adj[v]:
                if w == par:
                    continue
                if w in visited:
                    return False
                visited.add(w)
                q.append((w,v))
        return len(visited)==n