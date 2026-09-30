class Solution:
    def isPalindrome(self, s: str) -> bool:
        alph = ""
        rev_alph = ""
        for n in range(len(s)):
            if s[n].isalnum():
                alph += s[n].lower()
            if s[-n-1].isalnum():
                rev_alph += s[-n-1].lower()
        print(alph)
        print(rev_alph)
        return alph == rev_alph