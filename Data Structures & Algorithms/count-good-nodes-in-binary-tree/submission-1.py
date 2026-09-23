# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.numGoodNodes = 0

        def findPath(root, prevMax):
            if not root:
                return

            # Track current max and pass down
            prevMax = max(prevMax, root.val)

            # Traverse left and right subtrees
            findPath(root.left, prevMax)
            findPath(root.right, prevMax)

            # Increment if valid path
            if root.val >= prevMax:
                self.numGoodNodes += 1

        findPath(root, -math.inf)
        return self.numGoodNodes