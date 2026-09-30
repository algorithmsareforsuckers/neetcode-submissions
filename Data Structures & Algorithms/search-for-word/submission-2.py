class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        counts = Counter(word)
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] in counts:
                    counts[board[i][j]] -= 1
        for key,val in counts.items():
            if val > 0:
                return False
        
        edges = defaultdict(list)
        prefix = ""
        for n,char in enumerate(word):
            for i in range(len(board)):
                for j in range(len(board[i])):
                    # For each character, we check for a match, see if it was adjacent to a prev
                    # match, then put all following matches as edges
                    if n == 0:
                        if board[i][j] == char and (i,j) not in edges[char]:
                            edges[char].append((i,j))
                    else:
                        for x,y in edges[word[n-1]]:
                            if abs(x-i) + abs(y-j) == 1 and board[i][j] == char and (i,j) not in edges[char]:
                                edges[char].append((i,j))

            if edges[char] == []:
                return False
        return True

