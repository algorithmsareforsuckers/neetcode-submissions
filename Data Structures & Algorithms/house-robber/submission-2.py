class Solution:
    def rob(self, nums: List[int]) -> int:
               # We need to build out the max you can have by the time you reach i-1, i-2, and i-1, and then max by i will be easy from that information
        if len(nums) <= 1:
            return max(nums)
        prev2, prev1 = nums[0], nums[1]

        for i in range(2,len(nums)):
            curr = max(prev2 + nums[i], prev1)

            prev2, prev1 = max(prev2,prev1), prev2+nums[i]
        return max(prev2, prev1)