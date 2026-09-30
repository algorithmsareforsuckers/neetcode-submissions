class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1: return True

        need = n-1
        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= need:
                need = i
        return nums[0] >= need
