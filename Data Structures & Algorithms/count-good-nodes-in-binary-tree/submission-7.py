# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # recurse left and right subtrees while tracking prevMax
        # at each node, if val >= currMax, increment count and update prevMax to currMax
        # in the end return the count

        count = 0

        def dfs(root, prevMax):
            nonlocal count
            if not root:
                return

            if root.val >= prevMax:
                count += 1
                prevMax = root.val

            dfs(root.left, prevMax)
            dfs(root.right, prevMax)

        dfs(root, root.val)
        return count

