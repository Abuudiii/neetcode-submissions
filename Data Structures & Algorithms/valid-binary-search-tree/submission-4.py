# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
    - we can establish a bound
        - current node n node.left <= n <= node.right
    - do this recursively for both left and right subtrees
    - return False if this property breaks otherwise True
'''

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, lowerBound, upperBound):
            if not root:
                return True

            if root.val >= upperBound or root.val <= lowerBound:
                return False

            return dfs(root.left, lowerBound, root.val) and dfs(root.right, root.val, upperBound)

        return dfs(root, -math.inf, math.inf)
            