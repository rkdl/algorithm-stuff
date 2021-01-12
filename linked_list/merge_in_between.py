# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


def get_list_tail(cur: ListNode) -> ListNode:
    while cur and cur.next:
        cur = cur.next
    return cur


class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        cur = list1
        for _ in range(0, a - 1):
            cur = cur.next
        from_ = cur
        for _ in range(a, b + 1):
            cur = cur.next
        to_ = cur
        to_next = to_ and to_.next
        
        from_.next = list2
        list2_tail = get_list_tail(list2)
        to_.next = list2_tail
        list2_tail.next = to_next
        
        return list1
