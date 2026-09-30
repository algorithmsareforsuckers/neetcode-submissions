class Tree:
    def __init__(self, is_word=False, children=None):
        self.is_word = is_word
        self.children = {} if children is None else children

class PrefixTree:

    def __init__(self):
        self.root = Tree()
        
    def find_child(l, children):
        if l in children: 
            return True, child
        return False, None

    def insert(self, word: str) -> None:
        children = self.root.children
        for l in word:
            if l in children:
                child = children[l]
            else: 
                children[l] = Tree()
                child = children[l]

            children = child.children

        # Child points at the node representing the last letter in the word
        child.is_word = True

    def _find_node(self, word):
        children = self.root.children
        for l in word:
            if l in children:
                child = children[l]
                children = child.children
            else:
                return False, None
        return True,child
        

    def search(self, word: str) -> bool:
        contains, child = self._find_node(word)
        return contains and child.is_word
        

    def startsWith(self, prefix: str) -> bool:
        contains, _ = self._find_node(prefix)
        return contains
        
        