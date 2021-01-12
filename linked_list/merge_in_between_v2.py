# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


def get_list_tail(cur: ListNode) -> ListNode:
    while cur and cur.next:
        cur = cur.next
    return cur

def list_node_offset(cur: ListNode, n: int) -> ListNode:
    for _ in range(n):
        cur = cur.next
    return cur


class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        from_ = list_node_offset(list1, a - 1)
        to_ = list_node_offset(from_, b - a + 1)
        to_next = to_ and to_.next

        from_.next = list2
        list2_tail = get_list_tail(list2)
        to_.next = list2_tail
        list2_tail.next = to_next

        return list1
