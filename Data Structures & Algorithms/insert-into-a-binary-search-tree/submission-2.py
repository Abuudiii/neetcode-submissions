# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
    - recursively go through left or right subtree
        - based off of insertion node val compared to current root.val
    - once no leaf node exists, we insert the new node
'''
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node = TreeNode(val)
        if not root:
            return node

        def dfs(root, node):
            if node.val < root.val:
                if not root.left:
                    root.left = node
                else:
                    dfs(root.left, node)

            if node.val > root.val:
                if not root.right:
                    root.right = node
                else:
                    dfs(root.right, node)

        dfs(root, node)
        return root

            
            
