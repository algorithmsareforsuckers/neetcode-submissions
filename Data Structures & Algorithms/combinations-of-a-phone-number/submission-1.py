class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "": return []
        d_to_c = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}

        prev = [""]
        curr = []

        for char in digits:
            pos = d_to_c[char]
            for s in prev:
                for c in pos:
                    curr.append(s + c)

            prev = curr
            curr = []
        
        return prev
