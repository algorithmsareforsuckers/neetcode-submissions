class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res  = []

        def isPalindrome(s):
            if s == "":
                return False
            rev = s[::-1]
            return s == rev
        
        def backtrack(curr, i, curr_res):
            if i >= len(s):
                if isPalindrome(curr) or curr == "":
                    curr_res.append(curr)
                    res.append(curr_res.copy())
                    curr_res.pop()
                    return
                else:
                    return # Invalid partition
                

            if isPalindrome(curr):
                # add curr here
                curr_res.append(curr)
                backtrack(s[i],i+1,curr_res)

                curr_res.pop() # don't yet end curr
                backtrack(curr + s[i], i+1, curr_res)
            else:
                backtrack(curr + s[i], i+1, curr_res)
            return
        
        backtrack("", 0, [])
        return res