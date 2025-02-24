class TreeNode:
    def __init__(self):
        self.next = {}
        self.eow = False

class WordDictionary:

    def __init__(self):
        self.root = TreeNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for letter in word:
            if letter not in curr.next:
                curr.next[letter] = TreeNode()
            
            curr = curr.next[letter]
        
        curr.eow = True

    def search(self, word: str) -> bool:

        def dfs(node: TreeNode, idx: int) -> bool:
            if idx >= len(word):
                return node.eow
            
            if word[idx] == '.':
                for letter in node.next:
                    if dfs(node.next[letter], idx + 1):
                        return True
                return False
            
            if word[idx] in node.next:
                return dfs(node.next[word[idx]], idx + 1)
            
            return False
        
        return dfs(self.root, 0)