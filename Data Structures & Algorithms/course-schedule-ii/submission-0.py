class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        output = []
        visited, cycle = set(), set()

        for dst, src in prerequisites:
            adj[dst].append(src)

        def checkCourses(course):
            if course in cycle:
                return False
            
            if course in visited:
                return True

            cycle.add(course)

            for prereq in adj[course]:
                if not checkCourses(prereq):
                    return False

            cycle.remove(course)
            visited.add(course)
            output.append(course)

            return True

        for c in range(numCourses):
            if not checkCourses(c):
                return []
        
        return output

                

        