class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prev = [0]*3
        prev[1] = -prices[0]

        for i in range(1, len(prices)):
            tmp = [0]*3
            # j == 0
            tmp[0] = max(prev[0], prev[2])
            
            # j == 1
            tmp[1] = max(prev[0] - prices[i], prev[1])

            # j == 2
            tmp[2] = prev[1] + prices[i]
            # This can be inaccurate: specifically on day 1 it will be negative
            # However, this never matters since we only keep max profits
            prev = tmp

        return max(prev)

