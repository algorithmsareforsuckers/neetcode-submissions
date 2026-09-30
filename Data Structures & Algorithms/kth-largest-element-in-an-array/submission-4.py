import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(left, right):
            nonlocal nums
            # 1. Pick a random index
            index = random.randint(left, right)
            # 2. Swap it to the end to get it out of the way
            nums[right], nums[index] = nums[index], nums[right]

            # 3. Proceed with standard Lomuto partition logic!
            pivot = nums[right]
            p = left
            for i in range(left, right):
                if nums[i] < pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            
            nums[p], nums[right] = nums[right], nums[p] # Now nums[p] is properly placed

            return p # Index of where the randomly selected pivot is.

        left = 0
        right = len(nums) - 1
        while left <= right:
            pth = partition(left, right)

            if pth == len(nums) - k:
                return nums[pth]
            if pth < len(nums) - k:
                left = pth + 1
            else:
                right = pth - 1
        
        return -1
