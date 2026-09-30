class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        buckets = [1] * len(nums)
        total = 1

        for j in range(len(nums)):
            buckets[j] = buckets[j] * total
            total = total * nums[j]

        total = 1
        for j in range(len(nums)):
            k = len(nums) - j - 1
            buckets[k] = buckets[k] * total
            total = total * nums[k]
        
        return buckets