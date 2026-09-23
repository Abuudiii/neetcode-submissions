# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int: 
        self.res = 0     
        def findPath(root):
            if not root:
                return 0

            leftHeight = findPath(root.left)
            rightHeight = findPath(root.right)

            self.res = max(self.res, leftHeight + rightHeight)
            return 1 + max(leftHeight, rightHeight)

        findPath(root)
        return self.res