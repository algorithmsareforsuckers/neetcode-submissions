class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        visited = set()
        ROWS = len(grid)
        COLS = len(grid[0])
        modified = False

        def process_fruit(r,c):
            nonlocal modified
            if min(r,c) < 0 or r >= ROWS or c >= COLS or (r,c) in visited or grid[r][c] == 0:
                return
            modified = True
            grid[r][c] = 2
            visited.add((r,c))
            q.append([r,c])
            return


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    visited.add((r,c))
                    q.append([r,c])

        t = 0
        while q:
            for _ in range(len(q)):
                r,c = q.popleft()
                process_fruit(r+1, c)
                process_fruit(r-1,c)
                process_fruit(r,c+1)
                process_fruit(r,c-1)
            if modified:
                t += 1
                modified = False

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1
        return t 