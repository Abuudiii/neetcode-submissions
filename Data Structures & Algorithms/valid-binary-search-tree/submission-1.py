# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def validBound(node, lower, upper):
            if not node:
                return True

            if lower < node.val and node.val < upper:
                return validBound(node.left, lower, node.val) and validBound(node.right, node.val, upper)
            else:
                return False


        return validBound(root, -math.inf, math.inf)
        