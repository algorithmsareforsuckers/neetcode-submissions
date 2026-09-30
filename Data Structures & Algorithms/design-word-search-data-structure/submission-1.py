class TrieNode:
    def __init__(self, is_word=False, children=None):
        if not children:
            self.children = {}
        else:
            self.children = children
    
        self.is_word = is_word

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        self.search_node = self.root
        

    def addWord(self, word: str) -> None:
        curr_node = self.root

        for l in word:
            children = curr_node.children
            if l not in children:
                children[l] = TrieNode()
            curr_node = children[l]

        curr_node.is_word = True
        return
        

    def search(self, word: str) -> bool:
        curr_node = self.search_node
        for i,l in enumerate(word):
            children = curr_node.children

            if l == ".":
                res = False
                for node in children.values():
                    self.search_node = node
                    res = res or self.search(word[i+1:])
                self.search_node = self.root
                return res

            if l not in children: 
                self.search_node = self.root
                return False
            curr_node = children[l]

        self.search_node = self.root
        return curr_node.is_word
        
