class Solution:
    def rob(self, nums: List[int]) -> int:
        # We need to build out the max you can have by the time you reach i-1, i-2, and i-1, and then max by i will be easy from that information
        if len(nums) <= 2:
            return max(nums)
        prev3, prev2, prev1 = nums[0], nums[1], nums[2]+nums[0]

        for i in range(3,len(nums)):
            curr = max(prev3 + nums[i], prev2 + nums[i], prev1)

            prev3, prev2, prev1 = prev2, prev1, curr
            #print(prev2,prev1)
        return max(prev2, prev1)