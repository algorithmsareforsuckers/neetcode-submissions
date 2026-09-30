class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {"(":")", "{":"}", "[":"]"}

        for char in s:
            if char in pairs:
                # new open, add to stack
                stack.append(char)
                continue
            if stack and char == pairs[stack[-1]]:
                # char is a closed, and matches the most recently opened
                stack.pop()
                continue
            
            # char is a closed, and doesn't match
            return False
        if stack:
            # some opens were never closed
            return False
        return True
            





