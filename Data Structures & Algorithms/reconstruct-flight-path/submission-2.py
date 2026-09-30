class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        postorder = []
        adj = defaultdict(list)
        for dep, des in tickets:
            adj[dep].append(des)

        for dests in adj.values():
            dests.sort(reverse=True)
        stack = ["JFK"]
        while stack:
            curr = stack[-1]
            if not adj[curr]:
                postorder.append(stack.pop())
            else:
                stack.append(adj[curr].pop())
            
        return postorder[::-1]