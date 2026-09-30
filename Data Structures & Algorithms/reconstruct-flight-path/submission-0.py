class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        rev_path = []
        adj = {}
        for dep, des in tickets:
            if dep not in adj:
                adj[dep] = []
            adj[dep].append(des)
        for dests in adj.values():
            dests.sort(reverse=True)
        

        def dfs(airport):
            min_dest = None
            if airport not in adj: 
                rev_path.append(airport)
                return

            while adj[airport]:
                min_dest = adj[airport].pop()
                if min_dest: dfs(min_dest)
            rev_path.append(airport)
            
            return
        
        dfs("JFK")
        rev_path.reverse()

        return rev_path

