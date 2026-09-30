class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        best = 0
        l = 0
        seen = {} # char, ind

        for r, char in enumerate(s):
            if char in seen:
                best = max(r - l, best) # this auto +1s the r-l, which normally needs to be done.
                l = max(l, seen[char] + 1)
            seen[char] = r

        best = max(best, len(s) - l)
        return best
            

                

