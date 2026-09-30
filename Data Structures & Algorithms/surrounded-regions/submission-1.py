class Solution:
    def solve(self, board: List[List[str]]) -> None:
        leave = {}
        n,m = len(board), len(board[0])

        def dfs(c,r):
            if (c,r) in leave: return 

            leave[(c,r)] = "O"

            if c+1 < n and board[c+1][r] == "O":
                dfs(c+1,r)
            
            #print(n,m, c-1, r)
            if c-1 >= 0 and board[c-1][r] == "O":
                dfs(c-1,r)
            
            if r+1 < m and board[c][r+1] == "O":
                dfs(c,r+1)
            
            if r-1 >= 0 and board[c][r-1] == "O":
                dfs(c,r-1)
            
            return
        

        for i in range(m): 
            if board[0][i] == "O": dfs(0,i)
            if board[-1][i] == "O": dfs(n-1,i)
        for j in range(n):
            if board[j][0] == "O": dfs(j,0)
            if board[j][-1] == "O": dfs(j,m-1)

        for i in range(n):
            for j in range(m):
                board[i][j] = "X"
                if (i,j) in leave:
                    board[i][j] = "O"
        
        return
