class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        res = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    # The amount contributed is 4 - number of
                    # adjacent land squares
                    l = [i, j-1] if j-1 >= 0 else False
                    r = [i, j+1] if j+1 <len(grid[0]) else False
                    d = [i+1, j] if i+1 < len(grid) else False
                    u = [i-1, j] if i-1 >= 0 else False


                    res += 4
                    if l and grid[l[0]][l[1]] == 1: res -= 1
                    if r and grid[r[0]][r[1]] == 1: res -= 1
                    if d and grid[d[0]][d[1]] == 1: res -= 1
                    if u and grid[u[0]][u[1]] == 1: res -= 1

        return res
