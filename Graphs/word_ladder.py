from typing import List

class Node:
    def __init__(self, word:str):
        self.word = word
        self.next = []
    
    def __repr__(self):
        return '<Node word:' + self.word + '>'

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # check if one letter diff (n^2 * m)
        def one_off(a: str, b: str) -> bool:
            off = 0
            for i in range(len(a)):
                if a[i] != b[i]:
                    if off > 0:
                        return False
                    off += 1
            return True

        wordList.append(beginWord)
        
        nodes = {}
        for i in range(len(wordList)):
            word = wordList[i]
            nodes[word] = n = Node(word)
            for j in range(i):
                m = nodes[wordList[j]]
                if one_off(n.word, m.word):
                    n.next.append(m)
                    m.next.append(n)

        wordList.pop()
        
        res = 0
        visit = set()

        def dfs(node: Node, depth: int) -> None:
            if node.word == endWord:
                nonlocal res
                res = depth
                return
            
            for nei in node.next:
                if nei not in visit:
                    visit.add(nei)
                    dfs(nei, depth + 1)

        dfs(nodes[beginWord], 1)

        return res