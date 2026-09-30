class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # idea: go backwards and keep track of a list of points you need to get to to be done
        if len(nums) == 1: return True
        curr = len(nums)-2
        wants = len(nums)-1 # we just need to hold the smallest want
        while curr > 0:
            if curr + nums[curr] >= wants:
                wants = curr
            curr -= 1     

        return nums[0] >= wants