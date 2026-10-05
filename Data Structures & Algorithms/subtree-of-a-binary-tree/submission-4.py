# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        '''
            - recurse left and right subtrees in root until we reach the starting of subroot
            - do a dfs together and check both left and right subtrees are equal for root and subroot
            - at any point if they arent, we return False
            - return True at the end
        '''
        if not subRoot:
            return True
        if not root:
            return False

        if self.isSameTree(root, subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

        
    # recurses subtrees and checks if they are the same
    def isSameTree(self, root, subRoot):
        if not root and not subRoot:
            return True

        if (root and not subRoot) or (subRoot and not root):
            return False
        
        if root.val != subRoot.val:
            return False

        return self.isSameTree(root.left, subRoot.left) and self.isSameTree(root.right, subRoot.right)

        
        

