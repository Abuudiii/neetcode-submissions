'''
- populate minHeap first node from each list
- we only need the first node since we have references for the remaining nodes through that
- while that minHeap is valid, build the list
- repeat with the remaining indices
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        minHeap = []
        heapq.heapify(minHeap)

        for i in range(len(lists)):
            if lists[i]:
                head = lists[i]
                heapq.heappush(minHeap, [head.val, i, head])

        while minHeap:
            value, i, leastNode = heapq.heappop(minHeap)
            curr.next = leastNode
            curr = curr.next
            nextNode = leastNode.next
            
            if nextNode: 
                heapq.heappush(minHeap, [nextNode.val, i, nextNode])
        
        return dummy.next
