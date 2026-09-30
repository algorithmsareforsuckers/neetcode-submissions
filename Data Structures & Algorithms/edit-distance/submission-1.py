class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        prev = [i for i in range(len(word1)+1)] #if word 2 is empty, then we have to remove all chars in word 2
        curr = [0]*(len(word1)+1)
        curr[0] = 1 # word 2 has 1 char, so we just need to add it

        for i, c2 in enumerate(word2):
            for j, c1 in enumerate(word1):
                if c1 == c2:
                    curr[j+1] = min(prev[j], 1+curr[j], 1+prev[j+1])
                else:
                    curr[j+1] = 1 + min(curr[j], prev[j], prev[j+1])
            print(prev, curr)
            prev = curr
            curr = [i+2]*(len(word1)+1)
        
        return prev[-1]
