class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        postorder = []
        adj = defaultdict(list)
        for dep, des in tickets:
            adj[dep].append(des)

        for dests in adj.values():
            dests.sort(reverse=True)
        

        def dfs(airport):
            while adj[airport]:
                dfs(adj[airport].pop())
            postorder.append(airport)
        
        dfs("JFK")

        return postorder[::-1]

