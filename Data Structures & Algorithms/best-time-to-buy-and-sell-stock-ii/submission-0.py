class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1: return 0
        r = 1
        l = 0

        res = 0
        while r < len(prices):
            if prices[r] <= prices[r-1]:
                res += prices[r-1] - prices[l]
                l = r
            r += 1
        res += prices[r-1] - prices[l]
        
        return res