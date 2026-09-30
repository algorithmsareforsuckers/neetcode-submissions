class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        bank = {"":True }
    
        curr = ""
        for char in s:
            curr = curr + char
            bank[curr] = False

            for word in wordDict:
                if (len(curr) >= len(word)) and (curr[-len(word):] == word):
                    bank[curr] = bank[curr] or bank[curr[:-len(word)]]
                
        
        return bank[s]