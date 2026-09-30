class Solution:
    def rob(self, nums: List[int]) -> int:
               # We need to build out the max you can have by the time you reach i-1, i-2, and i-1, and then max by i will be easy from that information
        if len(nums) <= 1:
            return max(nums)
        prev2, prev1 = 0,0

        for n in nums:
            curr = max(prev2 + n, prev1)

            prev2, prev1 = prev1,curr
        return prev1