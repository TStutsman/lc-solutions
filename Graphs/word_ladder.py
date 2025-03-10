from collections import deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # bfs tree of possibilities

        # possible letters for each idx
        poss = []
        for idx in range(len(beginWord)):
            poss.append(set())
            for word in wordList:
                poss[idx].add(word[idx])

        q = deque([beginWord])
        words = set(wordList)
        depth = 1

        def addNeighbors(word: str) -> None:
            for i in range(len(word)):
                for char in list(poss[i]):
                    if char == word[i]:
                        continue
                    
                    newWord = word[:i] + char + word[i+1:]
                    if newWord in words:
                        words.discard(newWord)
                        q.append(newWord)

        while q:
            for _ in range(len(q)):
                curr = q.popleft()

                if curr == endWord:
                    return depth

                addNeighbors(curr)
            depth += 1
        
        return 0