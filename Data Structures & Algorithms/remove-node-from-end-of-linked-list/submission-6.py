# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
            - slow and fast pointer
            - after fast pointer reaches the end, remove the slow pointer node
            - return dummy head
        '''
        dummy = ListNode(0, head)
        prev = dummy
        curr = head

        # get fast n nodes away from slow
        while n:
            curr = curr.next
            n -= 1

        while curr:
            prev = prev.next
            curr = curr.next

        prev.next = prev.next.next

        return dummy.next

        

        


