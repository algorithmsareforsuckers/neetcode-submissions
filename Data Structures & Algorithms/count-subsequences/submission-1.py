class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # Bottom Up

        dp = [[0]*(len(s)+1) for _ in range(len(t) + 1)]

        # Row 1 is all 1s, since if t is empty, then this is 1
        dp[0] = [1]*(len(s)+1)

        len_s, len_t = len(s), len(t)
        for i, ct in enumerate(t):
            for j, cs in enumerate(s):
                t_ind, s_ind = len_t - 1 - i, len_s - 1 - j
                if t[t_ind] == s[s_ind]:
                    dp[i+1][j+1] = dp[i][j] + dp[i+1][j] # We either take this char or don't
                else:
                    dp[i+1][j+1] = dp[i+1][j] # We are not able to take this char
        
        return dp[-1][-1]
