

def subarray_sum(arr, target):
    for i in range(len(arr)):
        acc = 0
        for j in range(i, -1, -1):
            acc += arr[j]
            if acc == target:
                return (j, i)
    return None


print(subarray_sum([1,2,3], 2))
