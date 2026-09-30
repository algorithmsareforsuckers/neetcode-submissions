class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        A = [1] + nums + [1]
        n = len(A)

        dp = [[0]*(n) for _ in range(n)]
        
        for i in range(n-2,0,-1):
            for j in range(i, n-1):

                base = A[i-1]*A[j+1]
                max_coins = 0
                for k in range(i, j+1):
                    left = dp[i][k-1]
                    right = dp[k+1][j]

                    coins = left + right + (base * A[k])
                    if coins > max_coins: max_coins = coins

                dp[i][j] = max_coins 
                
        return dp[1][n-2]