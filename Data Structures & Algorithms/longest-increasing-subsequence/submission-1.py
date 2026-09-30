class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [[-1]*(n+1) for _ in range(n)]
        def recur(i, j):
            if i >= len(nums):
                return 0
            
            if memo[i][j+1] > -1: return memo[i][j+1]
            
            take = 0
            if j == -1 or nums[i] > nums[j]:
                take = 1 + recur(i+1,i)
                memo[i][j+1] = max(memo[i][j+1], take)
            
            leave = recur(i+1, j)
            memo[i][j+1] = max(memo[i][j+1], leave)
            return max(take, leave)
        
        return recur(0, -1)


            
            
                
