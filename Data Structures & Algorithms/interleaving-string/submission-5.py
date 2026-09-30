class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if s1 == s2 == s3 == "": return True
        if len(s1) + len(s2) != len(s3): return False

        prev = [False]*(len(s2)+1)
        prev[0] = True
        k = 0
        while k < len(s2):
            prev[k+1] = (s2[k] == s3[k] and prev[k])
            k += 1

        for i in range(len(s1)):
            curr = [False]*(len(s2)+1)
            curr[0] = prev[0] and s1[i] == s3[i]

            for j in range(len(s2)):
                curr[j+1] = (curr[j] and s2[j] == s3[i+j+1]) or (prev[j+1] and s1[i] == s3[i+j+1])
            prev = curr
        
        return prev[-1]

