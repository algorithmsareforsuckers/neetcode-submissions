class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0: return 1

        dp = [[0]*(amount+1) for _ in range(len(coins)+1)]
        dp[0][0] = 1 # with no coins, you can achieve the value 0, and nothing else

        for i in range(1, len(coins)+1):
            for amt in range(0, amount+1):
                dp[i][amt] = dp[i-1][amt]
                
                curr, k = amt-coins[i-1], 1
                while curr >= 0:
                    dp[i][amt] += dp[i-1][curr]
                    k += 1
                    curr = amt- coins[i-1]*k
            


            #print(i, dp[i])
                
        return dp[-1][amount]
