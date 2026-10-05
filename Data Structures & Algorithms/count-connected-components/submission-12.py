class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        seen = set()
        adj = defaultdict(list)
        components = 0

        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)

        
        def dfs(node):
            if node in seen:
                return 0

            seen.add(node)
            for nei in adj[node]:
                dfs(nei)

            return 1

        for i in range(n):
            components += dfs(i)

        return components
        