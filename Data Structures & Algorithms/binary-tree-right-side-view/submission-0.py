# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
    - bfs approach
    - start queue each node into a deque
    - push left then right
    - naturally end up with the right one
    - add it to res
'''

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
            
        res = []
        nextLevel = deque(
            [
                root
            ]
        )

        while nextLevel:
            currLevel = nextLevel
            nextLevel = deque()
            rightNode = None

            while currLevel:
                node = currLevel.popleft()

                if node:
                    rightNode = node

                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)

            if rightNode:
                res.append(rightNode.val)

        return res


        