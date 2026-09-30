class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        best = nums[0]

        curr = 0
        for i in range(len(nums)):
            curr += nums[i]
            best = max(curr, best)
            if curr < 0:
                if i == len(nums) - 1: return best # we can't even start something new
                curr = 0
        return best

            
