from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        opens = set(("(", "[", "{"))
        corr = {"(":")", "[":"]","{":"}"}

        for char in s:
            if char in opens:
                print("yes")
                stack.append(char)
            elif len(stack) == 0 or corr[stack[-1]] != char:
                return False
            else:
                stack.pop()
        
        if len(stack) != 0:
            return False
        return True

