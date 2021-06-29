# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from queue import PriorityQueue


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        pq = PriorityQueue()
        
        i = 0
        for l in lists:
            cur = l
            while cur:
                pq.put((cur.val, i, cur))
                cur = cur.next
                i += 1
        
        sentinel = ListNode(None)
        cur = sentinel
        while pq.qsize() > 0:
            _, _, n = pq.get()
            cur.next = n
            cur = n

        return sentinel.next
