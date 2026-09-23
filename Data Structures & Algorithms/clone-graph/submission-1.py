"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
            
        copied = {}
        visited = set()
        
        def dfs(node):
            if node in visited or not node:
                return

            visited.add(node)
            copied[node.val] = Node(node.val)

            for n in node.neighbors:
                dfs(n)

        dfs(node)
        print(copied)
        
        for n in visited:
            copiedNode = copied[n.val]
            
            for neighbor in n.neighbors:
                copiedNode.neighbors.append(copied[neighbor.val])

        return copied[1]

