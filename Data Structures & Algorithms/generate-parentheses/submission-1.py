class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(curr, num_open, num_close):
            if len(curr) >= 2*n:
                res.append(curr)
                return
            
            if num_open < n:
                backtrack(curr + "(", num_open + 1, num_close)
            if num_close < num_open:
                backtrack(curr + ")", num_open, num_close + 1)
            return
        
        backtrack("", 0, 0)
        return res