class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == "":
            return True

        searching = True
        n=0
        rev_n = len(s) - 1
        char = "" 
        rev_char = ""
        while searching:
            if char == "":
                if s[n].isalnum():
                    char = s[n].lower()
                elif n < len(s):
                    n += 1
            if rev_char == "":
                if s[rev_n].isalnum():
                    rev_char = s[rev_n].lower()
                elif rev_n > 0:
                    rev_n -= 1
            
            if char != "" and rev_char != "":
                if char != rev_char:
                    return False
                char = ""
                rev_char = ""
                if n < len(s):
                    n += 1
                if rev_n > 0:
                    rev_n -= 1
            
            if n == len(s) and rev_n == 0:
                searching = False
        return True