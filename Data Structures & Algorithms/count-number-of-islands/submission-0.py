class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0

        def dfs(x, y):
            if (x >= len(grid[0])) or (y >= len(grid)) or (x < 0) or (y < 0) or grid[y][x] == '0':
                return []

            grid[y][x] = '0'
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    count += 1
                    dfs(j,i)
        
        return count

            