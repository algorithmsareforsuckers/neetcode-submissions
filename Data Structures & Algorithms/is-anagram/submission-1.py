class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        if len(s) == len(t) == 0:
            return True
        
        counts = {}
        for c in s:
            counts[c] = counts.get(c, 0) + 1
        
        for c in t:
            counts[c] = counts.get(c,0) - 1

            if counts[c] < 0:
                return False
        
        return True
        