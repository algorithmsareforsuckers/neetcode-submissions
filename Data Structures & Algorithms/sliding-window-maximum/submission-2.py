class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        mx = float('-inf')
        second = 0

        h = []

        for r  in range(k):
            heapq.heappush(h, (-nums[r],r))
        
        res = [-h[0][0]]
        for r in range(k, len(nums)):
            while h and (r-h[0][1]) > (k-1):
                heapq.heappop(h)
            
            heapq.heappush(h, (-nums[r], r))
            
            res.append(-h[0][0])
        
        return res
