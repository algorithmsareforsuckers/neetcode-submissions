class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {-1:-1, 0:0}


        i = 1
        rem = amount
        while i <= amount:
            dp[i] = float('inf')
            for c in coins:
                curr = max(-1, i - c)
                    
                if dp[curr] >= 0:
                    dp[i] = min(dp[curr] + 1, dp[i])
                #if i == 1: print(dp[i])
            i += 1
        
        if dp[amount] == float('inf'): return -1
        return dp[amount]
