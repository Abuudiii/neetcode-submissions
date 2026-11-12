"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        '''
            1. go through each node and create a copy of it in the map
            2. go through list again linking each node to its appropriate copy
            3. return the copied head of the linked list
        '''
        mapping = {}
        mapping[None] = None

        # 1
        curr = head
        while curr:
            mapping[curr] = Node(curr.val)
            curr = curr.next

        # 2
        curr = head
        while curr:
            copied = mapping[curr]
            copied.next = mapping[curr.next]
            copied.random = mapping[curr.random]
            curr = curr.next

        # 3
        curr = head
        return mapping[curr]










