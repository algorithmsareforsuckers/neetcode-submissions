class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(curr, i, closures, k):
            nonlocal res
            print(curr)
            if i > 2*n:
                #curr = curr + ")"*closures
                copy = curr
                res.append(copy)
                return
            
            if k > 0:
                backtrack(curr + ")", i+1, closures, k-1)
                if closures < n:
                    backtrack(curr + "(", i+1, closures+1, k+1)
            elif closures < n:
                backtrack(curr + "(", i+1, closures+1, k+1)
            return
        
        backtrack("", 1, 0, 0)
        return res