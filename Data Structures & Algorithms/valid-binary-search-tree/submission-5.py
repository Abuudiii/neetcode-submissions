class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, lowerBound, upperBound):
            if not node:
                return True
            if not (lowerBound < node.val < upperBound):
                return False
            return dfs(node.left, lowerBound, node.val) and dfs(node.right, node.val, upperBound)

        return dfs(root, -math.inf, math.inf)