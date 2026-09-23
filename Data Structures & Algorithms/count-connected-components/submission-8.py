class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        '''
            - build adj list for all nodes in edges
            - use a set to track what nodes have been visited
            - recursively go through the adj list until a component is exhausted
            - each time increment components count by 1
            - if a node is already visited skip it
        '''
        visited = set()
        components = 0

        # build adj list
        adj = defaultdict(list)

        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)

        def dfs(node):
            if node in visited:
                return 0

            visited.add(node)

            for n in adj[node]:
                dfs(n)

            return 1

        for node in adj:
            components += dfs(node)

        if len(visited) < n:
            components += n - len(visited)

        return components

        
        







