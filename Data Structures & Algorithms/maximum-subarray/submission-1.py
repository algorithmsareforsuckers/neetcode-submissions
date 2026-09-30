class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        best = nums[0]
        r = 0

        curr = 0
        while r < len(nums):
            curr += nums[r]
            best = max(curr, best)
            if curr < 0:
                if r == len(nums) - 1: return best # we can't even start something new
                curr = 0
            r += 1
        return best

            
