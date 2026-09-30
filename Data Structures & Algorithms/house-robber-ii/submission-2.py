class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def path_robber(start, end):
            prev2, prev1 = 0,0

            for i in range(start, end):
                curr = max(prev2 + nums[i], prev1)

                prev2, prev1 = prev1,curr
            return prev1
        N = len(nums)
        return max(path_robber(1, N), path_robber(0, N-1))