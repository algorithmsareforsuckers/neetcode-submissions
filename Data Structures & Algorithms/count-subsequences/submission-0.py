class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        """
        Idea: Try DFS with memoization. 

        Ex. s = "caaat", t = "cat"

        We 'take' "c", then solve the problem on "aaat", "at". So on, proceeding depth first.
        As we go, we store our results in a map. In the future we may encounter a state that we've 
        already solved for, which will ensure efficiency.
        """
        memo = {}

        def dfs(s, t):
            if t == "":
                #print("t empty", s,t,0)
                return 1
            if s == "":
                #print("s empty", s,t,0)
                return 0
            
            if (s,t) in memo:
                #print("(s,t) in memo", s,t,memo[(s,t)])
                return memo[(s,t)]
            
            memo[(s,t)] = 0
            for i, char in enumerate(s):
                if char == t[0]:
                    next_s = s[i+1:]
                    next_t = t[1:]

                    if (next_s, next_t) in memo:
                        res = memo[(next_s, next_t)]
                    else:
                        res = dfs(next_s, next_t)

                    memo[(s,t)] += res

            #print("We found that ", s, t, " had ", memo[(s,t)], "possitilibies")
            return memo[(s,t)]

        return dfs(s,t)
