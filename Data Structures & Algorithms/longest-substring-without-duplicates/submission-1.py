class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # immediately I think sliding window
        if len(s) < 2:
            return len(s)
        r = 1
        l = 0
        best = 0
        last_seen = {}

        for j in range(len(s)):
            if s[j] in last_seen: 
                l = max(l, last_seen[s[j]] + 1)
                
            last_seen[s[j]] = j
            
            if r - l > best:
                best = r - l
            r += 1
        return best
            