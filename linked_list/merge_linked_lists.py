# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        new_list_head = ListNode(None)
        
        cur = new_list_head
        while l1 or l2:
            if not l2 or (l1 and l1.val <= l2.val):
                cur.next = l1
                l1 = l1.next
            elif l2:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
                
        return new_list_head.next
