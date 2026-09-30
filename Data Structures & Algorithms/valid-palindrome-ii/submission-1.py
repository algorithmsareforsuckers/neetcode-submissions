class Solution:
    def validPalindrome(self, s: str) -> bool:
        def val(l,r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        l,r = 0, len(s)-1
        removed_one = False

        while l < r:
            if s[l] != s[r]:
                if removed_one:
                    return False
                else:
                    return val(l+1, r) or val(l, r-1)
            l += 1
            r -= 1
        return True
                
