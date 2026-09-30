from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == "" or t == "": return ""
        counts = Counter(t)
        needed = len(t)

        r = 0
        while r < len(s)-1 and s[r] not in counts:
            r += 1
        l = r

        best = (0,float('inf'))
        while l < len(s) and r < len(s):
            if needed > 0:
                if s[r] in counts:
                    counts[s[r]] -= 1
                    if counts[s[r]] >= 0:
                        needed -= 1
            if needed == 0:
                b = best[1] - best[0]
                c = r+1 - l
                if c < b: best = (l, r+1)
                if s[l] in counts:
                    counts[s[l]] += 1
                    if counts[s[l]] > 0:
                        needed += 1
                        
                l += 1
            if needed > 0:
                r += 1
                
        
        if best[1] == float('inf'): return ""
        return s[best[0]:best[1]]
            


        




        