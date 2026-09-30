class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0: return 1
        curr = [0]*(amount+1)
        curr[0]=1

        for i in range(1, len(coins)+1):
            for amt in range(0, amount+1):
                if amt-coins[i-1] >= 0:
                    curr[amt] += curr[amt-coins[i-1]]
                prev = curr
                #print(curr)
                    
        return curr[amount]