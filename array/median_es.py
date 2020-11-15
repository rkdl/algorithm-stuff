from typing import *


def med(arr: List[int], l: int, r: int) -> float:
    size = r - l
    if size % 2 == 1:
        return arr[l + size // 2]

    i1 = l + size // 2
    i2 = i1 + 1
    return (arr[i1] + arr[i2]) / 2


def median_two(arr1: List[int], arr2: List[int]) -> float:
    assert len(arr1) == len(arr2)
    
    l1 = 0
    l2 = 0
    r1 = len(arr1)
    r2 = r1

    while True:
        print(f'l1: {l1}; r1: {r1}; l2: {l2}; r2: {r2}')

        size = r1 - l1
        print(f'size: {size}')
        print(f'size2: {r2 - l2}')
        if size == 1:
            return (arr1[0] + arr2[0]) / 2
        if size == 2:
            return (max(arr1[0], arr2[0]) + min(arr1[1], arr2[1])) / 2

        m1 = med(arr1, l1, r1)
        m2 = med(arr2, l2, r2)

        print(f'M1: {m1}; M2: {m2}')
        print('')
        if m1 == m2:
            return m1

        if m1 < m2:
            l1 = r1 // 2
            r2 = r2 // 2
        else:
            l2 = r2 // 2
            r1 = r1 // 2

    
print(median_two([3, 7, 8, 9, 20], [3, 4, 6, 15, 25]))
