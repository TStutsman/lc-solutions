from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # checking for loops in directional graph
        
        # courses dictionary
        # add prerequisites for each course
        # iterate over all courses
            # flip canFinish flag for courses that can be completed
            # for every prereq in course
                # check if canFinish
                # check if prereq canFinish

        untaken = {i:list() for i in range(numCourses)}
        for course, prereq in prerequisites:
            untaken[course].append(prereq)
        
        visit = set()

        def dfs(course: int) -> None:
            # course was already taken
            if course not in untaken:
                return True

            if course in visit:
                return False
            visit.add(course)
            
            # take all prereqs first
            for prereq in untaken[course]:
                if not dfs(prereq):
                    return False

            # all prereqs satisified -> take course
            del untaken[course]
            return True
        
        for course in range(numCourses):
            dfs(course)
        
        return len(untaken) == 0