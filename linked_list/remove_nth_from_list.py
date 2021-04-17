# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        sentinel = ListNode(None, head)

        back = sentinel
        front = sentinel

        i = 0
        while front and i < n:
            front = front.next
            i += 1

        while front and front.next:
            back = back.next
            front = front.next

        if back.next:
            back.next = back.next.next

        return sentinel.next
