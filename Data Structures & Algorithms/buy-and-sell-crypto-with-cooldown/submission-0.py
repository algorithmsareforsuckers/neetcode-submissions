class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0]*3 for _ in range(len(prices))]
        # for each day, we track profit with 0 holding, 1 holding, and cooldown
        dp[0][1] = -prices[0]
        
        for i in range(1, len(prices)):
            # j == 0
            dp[i][0] = max(dp[i-1][0], dp[i-1][2])
            
            # j == 1
            dp[i][1] = max((dp[i-1][0] - prices[i]), dp[i-1][1])

            # j == 2
            dp[i][2] = dp[i-1][1] + prices[i]
            # This can be inaccurate: specifically on day 1 it will be negative
            # However, this never matters since we only keep max profits
            #print(dp[i])

        return max(dp[-1])


