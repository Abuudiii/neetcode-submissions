# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        '''
            - start at root and recurse left and right subtrees
            - at any given valid root, we know that that node itself will count as 1
            - recurse down while tracking this paths depth
            - at base case, record it as max
        '''

        def dfs(root):
            if not root:
                return 0

            maxDepth = 1

            maxDepth = max(maxDepth + dfs(root.left), maxDepth + dfs(root.right))
            return maxDepth


        return dfs(root)