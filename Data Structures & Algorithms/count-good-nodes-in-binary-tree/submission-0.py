# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.numGoodNodes = 0

        def findPath(root, lastVal, prevMax):
            if not root:
                return

            # Track current max and pass down
            prevMax = max(prevMax, root.val)

            # Traverse left and right subtrees
            findPath(root.left, root.val, prevMax)
            findPath(root.right, root.val, prevMax)

            # Increment if valid path
            if root.val >= lastVal and root.val >= prevMax:
                self.numGoodNodes += 1

        findPath(root, root.val, -math.inf)
        return self.numGoodNodes


              

            


