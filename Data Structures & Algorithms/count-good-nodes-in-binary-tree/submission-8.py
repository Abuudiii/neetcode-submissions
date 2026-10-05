# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        goodNodes = 0
        
        def dfs(root, prevMax):
            nonlocal goodNodes

            if not root:
                return 

            if root.val >= prevMax:
                prevMax = root.val
                goodNodes += 1

            dfs(root.left, prevMax)
            dfs(root.right, prevMax)

        dfs(root, -math.inf)
        return goodNodes

