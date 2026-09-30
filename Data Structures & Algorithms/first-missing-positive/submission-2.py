class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            n = nums[i]
            if n == float('inf'):
                i += 1
                continue

            if 0 >= n or n >= len(nums)+1:
                i += 1
                continue
            # n is between 1 and len(nums)
            if n <= i+1:
                nums[n-1] = float('inf')
                i += 1
                continue
            
            # n is between i+1 and len(nums)
            # popcorn fill the higher numbers
            tmp = nums[n-1]
            while True:
                if nums[n-1] == float('inf'):
                    break
                nums[n-1] = float('inf')

                if 0 >= tmp or tmp >= len(nums)+1:
                    #out of range
                    break

                if tmp <= i+1:
                    nums[tmp-1] = float('inf')
                    break
                
                # tmp is between i+1 and len(nums)
                n = tmp
                tmp = nums[n-1]
            
            i += 1

        for i in range(len(nums)):
            if nums[i] != float('inf'):
                return i+1
        return len(nums)+1
                
                    

            


