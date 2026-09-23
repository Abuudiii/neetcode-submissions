# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # recurse left and right subtrees
        # at each node, see if nodes value is within upper and lower bounds
        # at base case return True meaning whole tree is valid

        def dfs(root, upperBound, lowerBound):
            if not root:
                return True

            if lowerBound >= root.val or root.val >= upperBound:
                return False

            return dfs(root.left, root.val, lowerBound) and dfs(root.right, upperBound, root.val)

        return dfs(root, math.inf, -math.inf)        
 