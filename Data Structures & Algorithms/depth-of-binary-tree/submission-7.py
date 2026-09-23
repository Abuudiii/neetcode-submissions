# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(root, currDepth):
            if not root:
                self.res = max(self.res, currDepth)
                return

            dfs(root.left, currDepth + 1)
            dfs(root.right, currDepth + 1)


        dfs(root, 0)
        return self.res