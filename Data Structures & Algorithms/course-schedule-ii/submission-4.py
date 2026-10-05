class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visited = set()
        cycle = set()
        adj = defaultdict(list)
        res = []

        for course, prereq in prerequisites:
            adj[course].append(prereq)

        def dfs(course):
            if course in visited:
                return True

            if course in cycle:
                return False

            cycle.add(course)

            for pre in adj[course]:
                if not dfs(pre):
                    return False

            cycle.remove(course)
            visited.add(course)
            res.append(course)
            
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return res

            
