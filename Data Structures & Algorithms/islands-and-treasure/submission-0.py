class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        def dfs(i,j, prev):
            if (not (0 <= i < len(grid))) or (not (0 <= j < len(grid[i]))) or grid[i][j] == -1:
                return
            
            if prev > grid[i][j]:
                return
            grid[i][j] = prev
            dfs(i+1, j, prev+1)
            dfs(i-1, j, prev+1)
            dfs(i, j+1, prev+1)
            dfs(i, j-1, prev+1)
            return

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    dfs(i,j,0)
        
        return