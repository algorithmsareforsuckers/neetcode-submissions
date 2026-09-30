class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        best = 0

        def dfs(i,j):
            if (not (0 <= i < len(grid))) or (not (0 <= j < len(grid[i]))) or (grid[i][j] == 0):
                return 0
            
            grid[i][j] = 0
            up = dfs(i, j-1)
            down = dfs(i, j+1)
            left = dfs(i-1, j)
            right = dfs(i+1, j)
            return 1 + up + down + left + right
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                best = max(best, dfs(i,j))
        return best