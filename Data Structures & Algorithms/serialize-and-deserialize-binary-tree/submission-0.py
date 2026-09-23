'''
    - pre-order traversal and serialize to string
    - count NULL nodes as N
    - build it back up in deserialization
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        output = []
        
        def dfs(root):
            if not root:
                output.append("N")
                return

            output.append(str(root.val))

            dfs(root.left)
            dfs(root.right)

        dfs(root)
        print(output)

        return ",".join(output)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        output = data.split(',')
        q = deque(output)
        
        def dfs():
            node = q.popleft()

            if node == "N":
                return None

            node = TreeNode(int(node))
            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()

        


        
