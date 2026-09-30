class Solution:

    def encode(self, strs: List[str]) -> str:
        enc = ""
        for s in strs:
            enc = enc + s
            enc = enc + "\u0394" # just include a non ascii char between strings
        
        return enc


    def decode(self, s: str) -> List[str]:
        dec = []
        curr = ""
        for char in s:
            if char == "\u0394":
                dec.append(curr)
                curr = ""
            else:
                curr = curr + char
        
        return dec
            
