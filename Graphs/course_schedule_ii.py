from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # array res for order
        # hash map for course prereqs
        # loop over map w/ visited set
            # dfs prereqs
                # if in visited return False
                # add to visited

                # if prereqs, dfs prereqs
                # if all prereqs met, add to res and return True
        
        # if len(res) == numCourses return res
        # else return []

        res = []
        prereqs = [list() for _ in range(numCourses)]

        for c, p in prerequisites:
            prereqs[c].append(p)
        
        def dfs(course: int) -> bool:
            if course in visit:
                return False
            visit.add(course)
            
            if prereqs[course] is not None:
                for prereq in prereqs[course]:
                    if not dfs(prereq): return False
                    
                prereqs[course] = None
                res.append(course)
            
            visit.discard(course)
            return True
        
        for course in range(numCourses):
            visit = set()
            if not dfs(course): return []
            
        return res