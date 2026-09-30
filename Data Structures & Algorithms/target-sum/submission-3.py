class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # need list of length 2*target + 1. indexes < target are neg, > target are pos
        s = sum(nums)
        if target > s: return 0
        l = 2*s+1
        prev = [0]*(l)
        prev[s] = 1 # with no numbers, there is 1 way to get to 0

        for num in nums:
            curr = [0]*(l)
            for val in range(l):
                if val - num >= 0:
                    curr[val] += prev[val - num] #take +num
                if val + num < l:
                    curr[val] += prev[val + num] #take -num
            prev = curr
        
        return curr[s + target]