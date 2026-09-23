'''
- create adjacency list
- keep track of visited until we find a loop or if we cant go further but still have numCourses being valid
'''

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites and numCourses:
            return True
        if not prerequisites:
            return False
        
        adjList = {}
        visited = set()
        safe = set()

        for postReq, preReq in prerequisites:
            if preReq not in adjList:
                adjList[preReq] = []
            if postReq not in adjList:
                adjList[postReq] = []
            
            adjList[preReq].append(postReq)

        
        def dfs(node, visited, adjList, safe):
            if node in visited:
                return False
            if not adjList[node]:
                return True
            if node in safe:
                return True

            visited.add(node)

            for postReq in adjList[node]:
                if not dfs(postReq, visited, adjList, safe):
                    return False

            visited.remove(node)
            safe.add(node)
            return True

        for preReq in adjList.keys():
            if not dfs(preReq, visited, adjList, safe):
                return False

        return True

