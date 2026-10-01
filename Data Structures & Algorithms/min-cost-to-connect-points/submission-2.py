class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        used = [False] * n
        best = [float("inf")] * n
        best[0] = 0
        total = 0

        def dist(p1,p2):
            return abs(p2[0]-p1[0]) + abs(p2[1]-p1[1])
        
        for _ in range(n):
            nxt = -1

            for i in range(n):
                if (not used[i]) and (nxt == -1 or best[i] < best[nxt]):
                    nxt = i
                
            total += best[nxt]
            used[nxt] = True

            # we just added nxt, so this could possible improve bests
            p2 = points[nxt]
            for i,p1 in enumerate(points):
                if i == nxt: continue
                best[i] = min(best[i], dist(p1,p2))
        
        return total

                    
