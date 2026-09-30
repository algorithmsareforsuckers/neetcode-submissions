class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) <= 1:
            return True
        r = len(s)-1
        l = 0

        while l <= r:
            while l <= r and not s[l].isalnum():
                l += 1
            
            print(l, r)
            if l > r:
                return True

            while l <= r and not s[r].isalnum():
                r -= 1

            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        
        return True
