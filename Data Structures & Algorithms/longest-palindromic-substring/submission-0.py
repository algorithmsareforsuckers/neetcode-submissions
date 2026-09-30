class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)==1:
            return s
        longest = 0
        best_start = 0

        def expand(left, right):
            nonlocal longest
            nonlocal best_start

            while left >= 0 and right <= len(s)-1 and s[left] == s[right]:
                left -= 1
                right += 1
            # r and l are off by one since we broke
            l = right - left - 1 # if they were both correct we'd need to add one, so here we subtract 1
            if l > longest:
                longest = l
                best_start = left+1
            return
        
        for i in range(len(s)):
            expand(i, i) #odd len
            expand(i, i+1)#even len
        
        return s[best_start:best_start + longest]
