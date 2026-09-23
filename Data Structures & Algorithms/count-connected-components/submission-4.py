'''
    - once a node has no further neighbours, we reached the end of a component
    - run dfs until component is exhausted, track visited nodes in set
'''

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        components = 0
        visited = set()
        adjList = defaultdict(list)

        for src, dst in edges:
            adjList[src].append(dst)
            adjList[dst].append(src)

        def dfs(node):
            if node in visited:
                return

            visited.add(node)

            for neighbor in adjList[node]:
                dfs(neighbor)


        for i in range(n):
            if i not in visited:
                dfs(i)
                components += 1
        
        return components


