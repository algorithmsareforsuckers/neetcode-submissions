class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums.count(0) > 1:
            return [0] * len(nums)

        buckets = [1]*len(nums)
        total = 1

        for j in range(len(nums)):
            if nums[j] == 0:
                buckets = [0] * len(nums)
                buckets[j] = 1
            else:
                total *= nums[j]
        

        for j in range(len(nums)):
            buckets[j] = buckets[j] * total
            if buckets[j] != 0 and nums[j] != 0:
                buckets[j] = int(buckets[j] / nums[j])

        return buckets