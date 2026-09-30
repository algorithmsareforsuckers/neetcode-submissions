class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        curr = [0]*(amount+1)
        curr[0]=1

        for i in range(1, len(coins)+1):
            for amt in range(0, amount+1):
                diff = amt - coins[i-1]
                if diff >= 0:
                    curr[amt] += curr[diff]
                    
        return curr[amount]