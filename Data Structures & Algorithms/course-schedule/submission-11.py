class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        seen = set()
        safe = set()
        adj = {}

        for course, pre in prerequisites:
            if course not in adj:
                adj[course] = []
            if pre not in adj:
                adj[pre] = []

            adj[course].append(pre)

        def dfs(course):
            if course in seen:
                return False

            if course in safe:
                return True

            seen.add(course)

            for pre in adj[course]:
                if not dfs(pre):
                    return False


            seen.remove(course)
            safe.add(course)
            return True

        for course in adj:
            if not dfs(course):
                return False

        return True
            