class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # core idea: loop 2 times, first mult everything to left of,
        # then everything to right of

        output = [1]*len(nums)

        for i, num in enumerate(nums):
            if i == 0:
                continue
            
            output[i] = output[i - 1] * nums[i - 1]
        
        tmp = [1]*len(nums)
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                print("start")
                continue
            
            tmp[i] = tmp[i+1] * nums[i + 1]
            output[i] *= tmp[i]
        
        return output