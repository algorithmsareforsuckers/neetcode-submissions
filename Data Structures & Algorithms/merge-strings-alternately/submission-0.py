class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        curr = 1
        mi = min(len(word1), len(word2))

        i = 0
        while i < 2*mi:
            ind = i // 2
            if curr == 1:
                res += word1[ind]
            else:
                res += word2[ind]
            
            i += 1
            curr = (curr + 1) % 2
        if len(word1) > len(word2):
            res += word1[mi:]
        if len(word2) > len(word1):
            res += word2[mi:]
        
        return res