from typing import List
from collections import defaultdict

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # curr = first letter
        # if prev:
            # add prev < curr to rules
        # recur all with same first letter
        # save as prev letter

        # for letter in rules:
            # if letter in visit:
                # continue
            # dfs to letter with no unvisited <
            # add to res, visit

        less_than = defaultdict(list)

        def dfs(similar: List[str], idx: int) -> None:
            prev = None
            sameLetter = []
            for word in similar:
                if idx >= len(word):
                    continue

                if prev and prev != word[idx]:
                    less_than[word[idx]].append(prev)
                    dfs(sameLetter, idx+1)
                    sameLetter = []

                prev = word[idx]
                sameLetter.append(word)

            if sameLetter:
                if prev not in less_than:
                    less_than[prev] = []
                dfs(sameLetter, idx+1)
        
        dfs(words, 0)

        visit = set()
        res = []
        def add_to_res(letter: str) -> None:
            if letter in less_than:
                for lesser in less_than[letter]:
                    if lesser not in visit:
                        visit.add(lesser)
                        add_to_res(lesser)
            res.append(letter)


        for let in less_than:
            if let in visit:
                continue
            visit.add(let)
            add_to_res(let)

        return "".join(res) 