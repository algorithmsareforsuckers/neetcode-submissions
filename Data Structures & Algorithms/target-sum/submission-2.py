class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # need list of length 2*target + 1. indexes < target are neg, > target are pos
        s = sum(nums)
        l = max(2*s+1, 2*target+1)
        prev = [0]*(l)
        prev[l//2] = 1 # with no numbers, there is 1 way to get to 0


        # notice that since we can add / subtract every num, the problem is 
        # symmetric w.r.t. sign of target
        for num in nums:
            curr = [0]*(l)
            for val in range(l): # val 0 represents -abs(target), 1 represents -abs(target) + 1, ...
                if val - num >= 0:
                    curr[val] += prev[val - num] #take +num
                if val + num < l:
                    curr[val] += prev[val + num] #take -num
            #print(prev, curr)
            prev = curr
        
        if 2*s + 1 > 2*target + 1:
            return curr[s + target]
        return curr[0]