from typing import Iterable, Iterator
from queue import PriorityQueue


# def merge_n_sorted(*sorted_streams: Iterable[int]) -> Iterator[int]:
#     stream_heads: list[tuple[int, Iterator[int]]] = []

#     for stream in sorted_streams:
#         stream_iter = iter(stream)
#         if stream_head := next(stream_iter, None):
#             stream_heads.append((stream_head, stream_iter))
    
#     while stream_heads:
#         min_el_idx, (min_el, min_el_stream) = min(enumerate(stream_heads), key=lambda x: x[1][0])

#         if next_head := next(min_el_stream, None):
#             stream_heads[min_el_idx] = (next_head, min_el_stream)
#         else:
#             stream_heads.pop(min_el_idx)

#         yield min_el

from functools import total_ordering


@total_ordering
class StreamHeadPair:
    stream_head: int
    stream: Iterator[int]

    def __init__(
        self,
        stream_head,
        stream,
    ):
        self.stream_head = stream_head
        self.stream = stream

    def __eq__(self, value):
        return self.stream_head.__eq__(value.stream_head)
    
    def __lt__(self, value):
        return self.stream_head.__lt__(value.stream_head)
    
    def __iter__(self):
        return iter((self.stream_head, self.stream))


def merge_n_sorted(*sorted_streams: Iterable[int]) -> Iterator[int]:
    min_heap = PriorityQueue()

    for stream in sorted_streams:
        stream_iter = iter(stream)
        if stream_head := next(stream_iter, None):
            min_heap.put(StreamHeadPair(stream_head, stream_iter))
    
    while not min_heap.empty():
        min_value, min_stream = min_heap.get()

        yield min_value

        next_head = next(min_stream, None)
        if next_head is not None:
            min_heap.put(StreamHeadPair(next_head, min_stream))

print([*merge_n_sorted([1,2,3], [1,1,2,3], [1,8, 15], [4, 13], [-1])])
