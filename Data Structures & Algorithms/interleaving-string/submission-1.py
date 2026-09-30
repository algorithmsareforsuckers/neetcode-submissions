class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if s1 == s2 == s3 == "": return True
        if len(s1) + len(s2) != len(s3): return False

        dp = [[False]*(len(s2)+1) for _ in range(len(s1)+1)] 
        # dp[i][j] answers the question of "can the first i letters of s1 and the
        # last j letter of s2 be interweaved to form the last i + j letters of s3"
        dp[0][0] = True
        k = 0
        while k < len(s1):
            dp[k+1][0] = (s1[k] == s3[k] and dp[k][0])
            k += 1
        k = 0
        while k < len(s2):
            dp[0][k+1] = (s2[k] == s3[k] and dp[0][k])
            k += 1


        #print(dp[0])
        for i in range(1, len(s1)+1):
            for j in range(1, len(s2)+1):
                dp[i][j] = (dp[i][j-1] and s2[j-1] == s3[i+j-1]) or (dp[i-1][j] and s1[i-1] == s3[i+j-1])
            #print(dp[i])
        
        return dp[-1][-1]


