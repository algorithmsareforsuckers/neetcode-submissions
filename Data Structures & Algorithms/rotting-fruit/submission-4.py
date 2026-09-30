class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        visited = set()
        ROWS = len(grid)
        COLS = len(grid[0])
        fresh = 0

        def process_fruit(r,c):
            nonlocal fresh
            if min(r,c) < 0 or r >= ROWS or c >= COLS or (r,c) in visited or grid[r][c] == 0:
                return
            grid[r][c] = 2
            visited.add((r,c))
            q.append([r,c])
            fresh -= 1
            return


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append([r,c])
                if grid[r][c] == 1:
                    fresh += 1

        t = 0
        while q:
            for _ in range(len(q)):
                r,c = q.popleft()

                directions = [(1,0), (-1,0), (0,1), (0,-1)]
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr, nc))
                        fresh -= 1
            if q:
                t += 1
            if fresh == 0:
                break
        print(fresh)
        return t if fresh == 0 else -1