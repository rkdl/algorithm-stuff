from typing import *
from dataclasses import dataclass


T = TypeVar('T')


@dataclass
class ListNode(Generic[T]):
    val: T
    next: Optional['ListNode[T]'] = None



class MyLinkedList:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.__sentinel = ListNode(0)
        self.__tail = None

    def __get_node_at(self, index: int) -> Optional[ListNode]:
        if index < 0:
            return None
        cur = self.__sentinel.next
        i = 0
        while cur and i < index:
            cur = cur.next
            i += 1
        return cur

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        node = self.__get_node_at(index)
        return node.val if node else -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self.__sentinel.next = ListNode(val, self.__sentinel.next)

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        cur = self.__sentinel
        while cur.next:
            cur = cur.next
        cur.next = ListNode(val)


    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        prev = self.__get_node_at(index - 1) if index != 0 else self.__sentinel
        if prev:
            prev.next = ListNode(val, prev.next)

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        prev = self.__get_node_at(index - 1) if index != 0 else self.__sentinel
        if prev:
            next_ = prev.next and prev.next.next
            prev.next = next_


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)