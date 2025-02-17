class TreeNode:
    def __init__(self):
        self.next = {}

class PrefixTree:
    # O(n) space
    def __init__(self):
        self.root = TreeNode()

    # O(n) insert
    def insert(self, word: str) -> None:
        curr = self.root
        for letter in word:
            if letter not in curr.next:
                curr.next[letter] = TreeNode()
            
            curr = curr.next[letter]

        curr.next['tail'] = None


    # O(n) search
    def search(self, word: str) -> bool:
        curr = self.root
        for letter in word:
            if letter not in curr.next:
                return False
            curr = curr.next[letter]
        
        if 'tail' not in curr.next:
            return False
        
        return True
        
    # O(n) lookup
    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for letter in prefix:
            if letter not in curr.next:
                return False
            curr = curr.next[letter]
        
        return True