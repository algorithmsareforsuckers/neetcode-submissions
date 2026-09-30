class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        ALPHABET = "abcdefghijklmnopqrstuvwxyz"
        words = set(wordList)
        seen = set([beginWord])

        q = deque([(beginWord, 1)])
        while q:
            #print(q, seen)
            curr, depth = q.popleft()
            for letter in ALPHABET:
                for i, char in enumerate(curr):
                    if letter == char: continue
                    alt = curr[:i] + letter + curr[i+1:]
                    if alt in words and alt not in seen:
                        if alt == endWord: return depth + 1
                        q.append((alt, depth + 1))
                        seen.add(alt)
        
        return 0
            


