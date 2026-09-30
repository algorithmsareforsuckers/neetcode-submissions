class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0: return 1

        dp = [[0]*(amount+1) for _ in range(len(coins)+1)]
        dp[0][0] = 1 # with no coins, you can achieve the value 0, and nothing else

        prev = [0]*(amount+1)
        prev[0] = 1

        curr = [0]*(amount+1)
        for i in range(1, len(coins)+1):
            for amt in range(0, amount+1):
                curr[amt] = prev[amt]
                if amt-coins[i-1] >= 0:
                    curr[amt] += curr[amt-coins[i-1]]
                prev = curr
                #print(curr)
                    
        return curr[amount]