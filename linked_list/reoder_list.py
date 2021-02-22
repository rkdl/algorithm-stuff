# https://leetcode.com/problems/reorder-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reverse_list(head):
        prev = None
        cur = head
        while cur:
            c = cur
            cur = cur.next
            c.next, prev = prev, c.next
            prev = c
        return prev


def find_mid(head):
    slow = head
    fast = head and head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next and fast.next.next
    return slow


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return

        mid = find_mid(head)
        desc_list = reverse_list(mid.next)
        mid.next = None  # break the list into two parts
        asc_list = head

        new_head_sentinel = ListNode()
        while asc_list or desc_list:
            if asc_list:
                new_head_sentinel.next = asc_list
                new_head_sentinel = new_head_sentinel.next
                asc_list = asc_list.next
            if desc_list:
                new_head_sentinel.next = desc_list
                new_head_sentinel = new_head_sentinel.next
                desc_list = desc_list.next
