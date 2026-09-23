# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
    - need a way to track the maximum at every point
    - if the current node's value is greater than max, its good otherwise its not
    - can recursively track this and add 1 to the res everytime we find a good node
'''

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0

        def dfs(root, maxVal):
            if not root:
                return

            maxVal = max(maxVal, root.val)

            dfs(root.left, maxVal)
            dfs(root.right, maxVal)

            if root.val >= maxVal:
                self.res += 1

        dfs(root, -math.inf)
        return self.res

            
             
