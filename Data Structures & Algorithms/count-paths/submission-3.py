class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if n == m == 1:
            return 1
        res = 0
        def valid_steps(m, n, prev):
            next_steps = {}
            for (x,y), count in prev.items():
                nonlocal res
                if x+1 < m:
                    next_steps[(x+1, y)] = next_steps.get((x+1,y), 0) + count
                if y+1 < n:
                    next_steps[(x, y+1)] = next_steps.get((x,y+1), 0) + count
            return next_steps
        

        # All paths are touch m + n - 1 points (including start and stop points)
        curr = {(0,0):1}
        for i in range(m+n-2): # we do -2 since (0,0) already taken
            curr = valid_steps(m,n,curr)
        
        return curr[(m-1, n-1)]


        


