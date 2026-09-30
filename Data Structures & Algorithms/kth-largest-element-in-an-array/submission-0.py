class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k_largest = heapq.nlargest(k, nums, key = lambda x: x)

        return k_largest[-1]