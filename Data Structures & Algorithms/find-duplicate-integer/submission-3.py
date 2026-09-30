class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        bigger = len(nums) * 10

        for i, n in enumerate(nums):
            nums[(n-1) % bigger] += bigger

        for i, n in enumerate(nums):
            if n >= 2 * bigger:
                return i + 1