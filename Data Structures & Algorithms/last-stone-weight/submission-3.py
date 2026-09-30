class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        
        heapq.heapify_max(stones)

        while len(stones) > 1:
            s1 = heapq.heappop_max(stones)
            s2 = heapq.heappop_max(stones)

            if s1 == s2: continue
            heapq.heappush_max(stones, abs(s1-s2))
        
        return stones[0] if stones else 0
