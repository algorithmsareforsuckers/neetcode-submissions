class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # Bottom up space optimized

        r_prev = [1]*(len(s) + 1)
        r_curr = [0]*(len(s) + 1)

        len_s, len_t = len(s), len(t)
        for i in range(len_t):
            for j in range(len_s):
                t_ind, s_ind = len_t - 1 - i, len_s - 1 - j
                if t[t_ind] == s[s_ind]:
                    r_curr[j+1] = r_prev[j] + r_curr[j] # We either take this char or don't
                else:
                    r_curr[j+1] = r_curr[j] # We are not able to take this char

            r_prev = r_curr
            r_curr = [0]*(len(s)+1)
        
        return r_prev[-1]