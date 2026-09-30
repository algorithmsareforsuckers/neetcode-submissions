class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        A = [1] + nums + [1]
        n = len(A)

        dp = [[0]*(n) for _ in range(n)]
        
        for i in range(n-2,0,-1):
            for j in range(i, n-1):


                for k in range(i, j+1):
                    left = dp[i][k-1]
                    right = dp[k+1][j]

                    gain = A[i-1] * A[k] * A[j+1]
                    dp[i][j] = max(dp[i][j], left + gain + right)
                
        return dp[1][n-2]