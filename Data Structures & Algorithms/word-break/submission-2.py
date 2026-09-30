class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        bank = [False]*(len(s)+1) #0th index is ''
        bank[0] = True
        for i in range(len(s)+1):
            for word in wordDict:
                if (len(word) <= i) and bank[i-len(word)]:
                    # Prefix is True
                    if s[i-len(word):i] == word:
                        bank[i] = True
        
        return bank[-1]