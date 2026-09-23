# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque([root])
        ans = []

        while q:
            tmp = []

            for i in range(len(q)):
                node = q.popleft()

                if node:
                    tmp.append(node.val)

                    nodeL, nodeR = node.left, node.right
                    if nodeL:
                        q.append(nodeL)
                    if nodeR:
                        q.append(nodeR)

                else:
                    break

            ans.append(tmp)

        return ans