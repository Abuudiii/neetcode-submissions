class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        visited, cycle = set(), set()
        adj = defaultdict(list)

        for course, pre in prerequisites:
            adj[course].append(pre)

        def dfs(course):
            if course in cycle:
                return False

            if course in visited:
                return True

            cycle.add(course)

            for pre in adj[course]:
                if not dfs(pre):
                    return False

            cycle.remove(course)
            visited.add(course)
            res.append(course)

            return True

        for c in range(numCourses):
            if not dfs(c):
                return []

        return res