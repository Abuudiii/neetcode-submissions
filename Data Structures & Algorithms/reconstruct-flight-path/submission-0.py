class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        tickets.sort()  # ensures lexical order when we pop from the end (see below)
        
        for src, dst in tickets:
            adj[src].append(dst)
        
        # reverse so we can pop() from the end in lexical order (O(1) instead of pop(0))
        for src in adj:
            adj[src].sort(reverse=True)
        
        res = []
        
        def dfs(airport):
            while adj[airport]:
                nxt = adj[airport].pop()
                dfs(nxt)
            res.append(airport)
        
        dfs("JFK")
        return res[::-1]