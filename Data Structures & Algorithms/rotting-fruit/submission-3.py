class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        
        # 1. Single setup pass to find rotten and count fresh
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))
                    
        t = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        # 2. If fresh == 0, this loop never runs (safely returns 0)
        #    If q runs out but fresh > 0, it exits early
        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    
                    # If neighbor is fresh, rot it!
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                        grid[nr][nc] = 2          # Mutating the grid acts as our "visited" set!
                        q.append((nr, nc))
                        fresh -= 1
            t += 1
            
        return t if fresh == 0 else -1