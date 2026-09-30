from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == "" or t == "": return ""
        counts = Counter(t)
        needed = len(t)

        l = 0

        best = float('inf')
        start_ind = 0
        for r in range(len(s)):
            if s[r] in counts:
                counts[s[r]] -= 1
                if counts[s[r]] >= 0:
                    needed -= 1

            while needed == 0:
                if (r+1-l) < best:
                    best = r+1 - l
                    start_ind = l

                if s[l] in counts:
                    counts[s[l]] += 1
                    if counts[s[l]] > 0:
                        needed += 1
                l += 1
        
        if best == float('inf'): return ""
        return s[start_ind:start_ind+best]