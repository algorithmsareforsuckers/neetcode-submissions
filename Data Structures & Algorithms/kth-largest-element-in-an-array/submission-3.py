class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k_large = nums[:k]
        heapq.heapify(k_large)
        print(k_large)

        for i, num in enumerate(nums[k:]):
            heapq.heappush(k_large, num)
            heapq.heappop(k_large)
        
        return k_large[0]