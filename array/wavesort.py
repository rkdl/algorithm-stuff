def wave(A):
    n = len(A)
    sorted_arr = sorted(A)
        
    new_arr = [0] * n
        
    last_i = n - 1
    for i, el in enumerate(sorted_arr):
        if i % 2 == 0:
            ins_idx = i
            if i < last_i:
                ins_idx += 1
        else:
            ins_idx = i - 1
        new_arr[ins_idx] = el
        
    return new_arr


def wave_v2(A):
    sorted_arr = list(sorted(A))
        
    for i in range(0, len(sorted_arr) - 1, 2):
        tmp = sorted_arr[i]
        sorted_arr[i] = sorted_arr[i + 1]
        sorted_arr[i + 1] = tmp
        
    return sorted_arr


print(wave_v2([5,1,3,2,4]))