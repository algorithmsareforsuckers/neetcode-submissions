class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        buckets = [1]*len(nums) # index j needs to be prod_{i\ne j} nums[i]

        tracker = {}
        zero_flag = None
        zero_count = 0
        total = 1

        for j in range(len(nums)):
            if nums[j] == 0:
                zero_flag = j
                zero_count += 1
            else:
                total *= nums[j]
            tracker[j] = 1
        
        if zero_count > 1:
            return [0] * len(nums)
        if zero_count == 1:
            buckets = [0] * len(nums)
            buckets[zero_flag] = total
            return buckets
        for j in range(len(nums)):
            buckets[j] = int(total / nums[j])




        
        return buckets

        