# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.__iterator = iterator

        if iterator.hasNext():
            self.__cur = iterator.next()
            self.__has_next = True
        else:
            self.__cur = None
            self.__has_next = False


    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.__cur

    def next(self):
        """
        :rtype: int
        """
        rval = self.__cur

        if self.__iterator.hasNext():
            self.__cur = self.__iterator.next()
            self.__has_next = True
        else:
            self.__cur = None
            self.__has_next = False

        return rval

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.__has_next

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
