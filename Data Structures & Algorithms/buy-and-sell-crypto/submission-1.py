class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        l = 0

        for r, price in enumerate(prices):
            best = max(best, (price - prices[l]))
            if price < prices[l]:
                l = r
        
        return best