class Solution:
    def findMin(self, nums: List[int]) -> int:
        # if we find the index of the max, min is either first element of 1 to right of max.
        maybe_min = nums[0]
        max_seen = 0
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = l + (r-l)//2

            if nums[mid] >= nums[max_seen]:
                max_seen = mid
                l = mid + 1
            else:
                r = mid - 1
        
        if max_seen >= len(nums) - 1:
            return nums[0]
        return nums[max_seen+1]
