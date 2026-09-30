import math
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1


        while l <= r:
            mid = l + (r-l) // 2
            value = nums[mid]

            if value == target:
                return mid
            if value > target:
                r = mid - 1
            else:
                l = mid + 1
            
        
        return -1