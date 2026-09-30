class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dists = []
        
        for x,y in points:
            dists.append((x**2 + y**2, [x,y])) # no need to take sqrt since its monotonic anyways
        if not points:
            return None
        heapq.heapify_max(dists)

        while len(dists) > k:
            heapq.heappop_max(dists)
        
        return [d[1] for d in dists]