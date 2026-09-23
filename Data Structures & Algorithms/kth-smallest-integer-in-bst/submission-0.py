# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
    - do an in-order traversal recursively
    - store values into an array
    - return 1 indexed kth smallest value
'''

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []

        def dfs(root):
            if not root:
                return None

            dfs(root.left)
            res.append(root.val)
            dfs(root.right)
        
        dfs(root)
        return res[k-1]