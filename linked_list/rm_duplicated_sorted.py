# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        prev = head
        cur = head and head.next
        while cur:
            if cur.val == prev.val:
                prev.next = cur.next
            else:
                prev = cur
            cur = cur.next
        return head
