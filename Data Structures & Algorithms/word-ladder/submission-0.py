class Vertex:

    def __init__(self, name=None, parent=None, depth=None):
        self.name = name
        self.parent = parent
        self.depth = depth
    


class Solution:
    def validPair(self, v, w):
        differences = 0
        for a,b in zip(v.name,w.name):
            if a != b:
                differences += 1
                if differences > 1: return False
        if differences == 0: return False
        return True
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Make graph where edge is a valid word transition
        # bfs from beginWord, first appearance of endWord marks the shortest path
        #if endWord not in wordList: return 0

        beg = Vertex(name=beginWord,depth=1)

        seen = set(beginWord)
        q = deque([beg])

        while q:
            curr = q.popleft()
            for word in wordList:
                v = Vertex(word, curr, curr.depth+1)
                if word not in seen and self.validPair(curr, v):
                    if v.name == endWord:
                        return v.depth

                    seen.add(word)
                    q.append(v)

        return 0
                

        
        