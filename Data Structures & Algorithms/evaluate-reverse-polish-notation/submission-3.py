class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def dfs(tokens):
            ops = set(("+", "-", "*", "/"))
            t = tokens.pop()
            if t not in ops:
                print(t)
                return int(t)
            
            r = dfs(tokens)
            print(tokens)
            l = dfs(tokens)
            print(tokens)

            if t == "+": return l + r
            if t == "-": return l - r
            if t == "*": return l * r
            if t == "/": return int(l/r)

        
        return dfs(tokens)
