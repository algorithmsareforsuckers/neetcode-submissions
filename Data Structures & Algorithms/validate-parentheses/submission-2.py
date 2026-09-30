class Solution:
    def isValid(self, s: str) -> bool:
        # ( ), { }, [ ]
        q = []
        opens = ("(", "[", "{")
        closed = {")": "(", "]": "[", "}":"{"}
        
        if s[0] not in opens or len(s) % 2 == 1:
            return False

        for char in s:
            if char in opens:
                q.append(char)
            elif len(q) == 0 or q[-1] != closed[char]:
                return False
            else:
                q.pop()


        if len(q) == 0:
            return True
        return False

                

            