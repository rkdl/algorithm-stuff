import math
from collections import deque

inp = [-8, -6, -4, 1, 2, 3, 5, 6]


def do_stuff(arr):
    out = [None] * len(inp)
    left_cursor = 0
    right_cursor = len(arr) - 1
    for i in range(len(arr) - 1, -1, -1):
        left = arr[left_cursor]
        right = arr[right_cursor]
        if abs(left) > abs(right):
            out[i] = left ** 2
            left_cursor += 1
        else:
            out[i] = right ** 2
            right_cursor -= 1
    return out


print(do_stuff(inp))
