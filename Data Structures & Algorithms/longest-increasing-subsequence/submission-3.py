from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = 1
        dp = [nums[0]]

        for i in range(1, len(nums)):
            if dp[-1] < nums[i]:
                res += 1
                dp.append(nums[i])
            
            else:
                idx = bisect_left(dp, nums[i])
                dp[idx] = nums[i]
        
        return res

        