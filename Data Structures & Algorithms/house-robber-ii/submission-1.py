class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def path_robber(nums):
            prev2, prev1 = 0,0

            for n in nums:
                curr = max(prev2 + n, prev1)

                prev2, prev1 = prev1,curr
            return prev1
        
        return max(path_robber(nums[1:]), path_robber(nums[:-1]))
