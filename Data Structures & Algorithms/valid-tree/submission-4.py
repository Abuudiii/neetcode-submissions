class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != (n - 1):
            return False

        visited = set()

        # adj list
        adj = defaultdict(list)

        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)

        # dfs method to traverse
        def dfs(node):
            if node in visited:
                return False

            visited.add(node)

            for neighbour in adj[node]:
                dfs(neighbour)

        # validate graph
        dfs(0)

        return len(visited) == n



        