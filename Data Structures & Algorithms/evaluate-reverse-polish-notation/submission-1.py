class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = ("+", "-", "/", "*")
        if len(tokens) <= 3:
            if len(tokens)==1:
                return int(tokens[0])
            return int(eval(tokens[0] + tokens[2] + tokens[1]))
        
        right = []
        left = []
        op = tokens.pop()
        
        r_done = False
        o_cnt = 1
        n_cnt = 0
        while not r_done:
            t = tokens.pop()
            if t in ops:
                o_cnt += 1
            else:
                n_cnt += 1
            right.append(t)
            if n_cnt == o_cnt:
                r_done = True
        print(right)
        right = right[::-1]
        print(right)
        r = self.evalRPN(right)
        

        l_done = False
        o_cnt = 1
        n_cnt = 0 
        while not l_done:
            t = tokens.pop()
            if t in ops:
                o_cnt += 1
            else:
                n_cnt += 1
            left.append(t)
            if n_cnt == o_cnt:
                l_done = True
        left = left[::-1]
        l = self.evalRPN(left)

        return int(eval(str(l) + op + str(r)))
        