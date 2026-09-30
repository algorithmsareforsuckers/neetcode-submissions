class Solution:
    def checkValidString(self, s: str) -> bool:
        s1 = []
        s2 = []

        for i, char in enumerate(s):
            if char == "(":
                s1.append(i)
            elif char == "*":
                s2.append(i)
            else:
                if s1:
                    s1.pop()
                elif s2:
                    s2.pop()
                else:
                    return False
        
        while s1 and s2:
            s1i = s1.pop()
            s2i = s2.pop()
            if s1i > s2i:
                return False
                

        return len(s1) == 0



            