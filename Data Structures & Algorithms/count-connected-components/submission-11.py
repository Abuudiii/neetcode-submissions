class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        components = 0
        adj = defaultdict(list)

        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)

        def dfs(node):
            if node in visited:
                return 0

            visited.add(node)

            for nei in adj[node]:
                dfs(nei)

            return 1

        for n in range(n):
            components += dfs(n)

        return components