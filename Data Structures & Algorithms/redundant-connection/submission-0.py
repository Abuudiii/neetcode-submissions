class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)

        def dfs(node, parent):
            if node in visited:
                return True

            visited.add(node)

            for nei in adj[node]:
                if nei == parent:
                    continue

                if dfs(nei, node):
                    return True

            return False

        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)
            visited = set()

            if dfs(src, -1):
                return [src, dst]

        return []