class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {}
        visited = set()
        valid = False

        for postReq, preReq in prerequisites:
            if postReq not in adjList:
                adjList[postReq] = []
            if preReq not in adjList:
                adjList[preReq] = []

            adjList[preReq].append(postReq)

        def dfs(course):
            if course in visited:
                return False

            visited.add(course)

            for neighbour in adjList[course]:
                if not dfs(neighbour):
                    return False

            visited.remove(course)

            return True


        for course in adjList:
            if not dfs(course):
                return False

        return True




        
