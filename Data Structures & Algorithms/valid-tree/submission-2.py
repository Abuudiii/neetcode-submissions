'''
    - compare len edges to n - 1, if its ot equal then its either disconnected or cycle exists
    - do dfs on the rest and see if we can visit every node, if so return true otherwise false
'''
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != (n - 1):
            return False

        visited = set()
        adjList = defaultdict(list)

        # Builds out neighbours
        for src, dst in edges:
            if src not in adjList:
                adjList[src] = []
            if dst not in adjList:
                adjList[dst] = []

            adjList[src].append(dst)
            adjList[dst].append(src)

        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)
            
            for neighbor in adjList[node]:
                dfs(neighbor)

        dfs(0)

        return len(visited) == n



        

        