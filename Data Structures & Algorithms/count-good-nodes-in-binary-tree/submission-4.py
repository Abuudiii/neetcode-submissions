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
        self.count = 0

        def dfs(root, currMax):
            if not root:
                return None
            
            if root.val >= currMax:
                currMax = root.val
                self.count += 1

            dfs(root.left, currMax)
            dfs(root.right, currMax)

        dfs(root, root.val)

        return self.count


            

