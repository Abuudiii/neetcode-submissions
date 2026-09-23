# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(None, head)
        
        leftPrev, curr = dummy, head

        for i in range(left - 1):
            leftPrev, curr = curr, curr.next

        prev = None
        for i in range(right - left + 1):
            nxt = curr.next

            curr.next = prev
            prev = curr
            curr = nxt


        leftNode = leftPrev.next
        leftNode.next = curr
        leftPrev.next = prev

        return dummy.next
        

