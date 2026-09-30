class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        mpt = [cost[0], cost[1]]
        i = 2

        while i < len(cost):
            mpt[1] = min(mpt[1], mpt[0]+cost[i-1])
            ith = min(mpt) + cost[i]
            mpt = [mpt[1], ith]
            i += 1
            
        return min(mpt) # the last step we are on is either the last one or the 2nd to last one
