class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def knapsack(amount):
            #print(amount)
            if amount == 0:
                return 0
            if amount < 0:
                return -1
            
            if amount in memo: return memo[amount]

            best = float('inf')
            for c in coins:
                curr = knapsack(amount-c)
                if curr >= 0:
                    best = min(best, curr+1)
            
            if best == float('inf'): best = -1
            memo[amount] = best
            return best
            
        
        return knapsack(amount)
            
