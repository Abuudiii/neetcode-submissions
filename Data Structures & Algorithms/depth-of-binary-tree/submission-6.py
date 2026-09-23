# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
    - recurse over left and right subtree
    - track number of nodes visited throughout
    - once we hit a leaf node, record current node count with previous max count
'''

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.depth = 0

        def dfs(root, currDepth):
            if not root:
                self.depth = max(self.depth, currDepth)
                return

            dfs(root.left, currDepth + 1)
            dfs(root.right, currDepth + 1)

        dfs(root, 0)
        return self.depth

        