class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        t=len(nums)
        for i in range(len(nums)):
            t += i - nums[i]
        return t