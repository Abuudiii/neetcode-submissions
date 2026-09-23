class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        safe = set()
        adj = {}

        for course, prereq in prerequisites:
            if course not in adj:
                adj[course] = []
            if prereq not in adj:
                adj[prereq] = []

            adj[course].append(prereq)

        def dfs(course):
            if course in visited:
                return False

            if course in safe:
                return True

            visited.add(course)

            for nei in adj[course]:
                if not dfs(nei):
                    return False

            visited.remove(course)
            safe.add(course)
            return True

        for course in adj:
            if not dfs(course):
                return False

        return True