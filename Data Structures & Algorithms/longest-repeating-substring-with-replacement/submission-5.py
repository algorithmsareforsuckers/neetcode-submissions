class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        best = 0
        l = 0
        counts = defaultdict(int)

        for r, char in enumerate(s):
            counts[char] += 1
            num_wrong = (r+1 - l) - max(counts.values()) #O(1) since len(counts.values() <= 26)
            while num_wrong > k:
                counts[s[l]] -= 1
                l += 1
                num_wrong -= 1
            
            best = max(best, r+1 - l) 
        
        return best