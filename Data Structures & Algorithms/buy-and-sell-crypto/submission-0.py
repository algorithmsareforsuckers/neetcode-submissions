class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_seen = 1e7

        profit = 0
        for i in range(len(prices)):
            min_seen = min(min_seen, prices[i])
            print(min_seen)
            profit = max(profit, prices[i] - min_seen)

        return max(profit, 0)