# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
    - recursively go down left and right subtrees
    - at each path track the currentMax
    - increment count accordingly
'''

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(root, currMax):
            if not root:
                return 0
            
            res = 0
            if root.val >= currMax:
                res = 1

            currMax = max(currMax, root.val)

            res += dfs(root.left, currMax)
            res += dfs(root.right, currMax)

            return res

        return dfs(root, root.val)

            

