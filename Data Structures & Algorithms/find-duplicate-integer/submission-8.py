class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = 1
        slow = 0

        for i, num in enumerate(nums):
           
            if nums[abs(num) - 1] < 0:
                return abs(num)
            nums[abs(num) - 1] *= -1

