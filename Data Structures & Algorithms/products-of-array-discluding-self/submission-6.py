class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # idea, do 2 loops through nums. First do everything to left of, then everything to right of

        left = [1]*len(nums)
        right = [1]*len(nums)

        for i in range(len(nums)):
            if i == 0:
                continue
            left[i] = left[i-1] * nums[i-1]

            r = len(nums) - i - 1
            right[r] = right[r+1] * nums[r+1]
        

        output = [1]*len(nums)
        for i in range(len(nums)):
            output[i] = left[i] * right[i]
        
        return output