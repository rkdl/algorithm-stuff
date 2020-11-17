# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def add_helper(l1: ListNode, l2: ListNode, rem: int) -> ListNode:
            if not l1 and not l2 and rem == 0:
                return None

            s = rem
            if l1:
                s += l1.val
            if l2:
                s += l2.val

            rem, cur_val = divmod(s, 10)
            next_ = add_helper(l1 and l1.next, l2 and l2.next, rem)
            return ListNode(cur_val, next_)

        return add_helper(l1, l2, 0)
