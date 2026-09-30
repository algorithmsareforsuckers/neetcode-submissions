class Solution:
    def rob(self, nums: List[int]) -> int:
        def path_robber(nums):
            if len(nums) <= 1:
                return max(nums)
            prev2, prev1 = 0,0

            for n in nums:
                curr = max(prev2 + n, prev1)

                prev2, prev1 = prev1,curr
            return prev1

        if len(nums) <= 3:
            return max(nums)
        # We have to figure out the max using index 0 and the max using index 1
        tmp = nums[0]
        nums[0] = float('-inf')
        without_zero = path_robber(nums)
        nums[0] = tmp
        nums[1] = nums[-1] = float('-inf')
        with_zero = path_robber(nums)
        return int(max(without_zero, with_zero))

            
