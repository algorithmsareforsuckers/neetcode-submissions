class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac_reach, pac = set(), deque()
        atl_reach, atl = set(), deque()
        ROWS, COLS = len(heights), len(heights[0])
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        
        #init pacific
        for c in range(len(heights[0])):
            pac_reach.add((0,c))
            pac.append([0,c])

            atl_reach.add((ROWS-1, c))
            atl.append([ROWS-1, c])
        for r in range(len(heights)):
            pac_reach.add((r,0))
            pac.append([r,0])

            atl_reach.add((r,COLS-1))
            atl.append([r, COLS-1])
        


        def multi_bfs(ocean_set, ocean_queue):
            while ocean_queue:
                for _ in range(len(ocean_queue)):
                    r,c = ocean_queue.popleft()
                    for dr, dc in dirs:
                        nr, nc = r+dr, c+dc
                        if (0 <= nr < ROWS) and (0 <= nc < COLS):
                            if (heights[nr][nc] >= heights[r][c]) and ((nr,nc) not in ocean_set):
                                ocean_queue.append([r+dr, c+dc])
                                ocean_set.add((r+dr,c+dc))
            return 
        
        multi_bfs(pac_reach, pac)
        multi_bfs(atl_reach, atl)

        res = []
        for tpl in pac_reach & atl_reach:
            res.append(list(tpl))
        return res