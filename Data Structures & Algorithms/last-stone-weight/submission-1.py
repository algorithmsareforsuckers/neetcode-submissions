class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones) > 1:
            s0 = heapq.heappop_max(stones)
            s1 = heapq.heappop_max(stones)
            if s0 > s1:
                heapq.heappush_max(stones, s0 - s1)
            
        if not stones:
            return 0
        return stones[0]
        