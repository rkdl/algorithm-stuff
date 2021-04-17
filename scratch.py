def bin_search(haystack, needle):
    l_idx = 0
    r_idx = len(haystack) - 1
    
    result = -1

    while l_idx <= r_idx:
        mid_idx = (l_idx + l_idx) // 2
        mid_val = haystack[mid_idx]
        if mid_val == needle:
            result = mid_idx
            break
        if mid_val < needle:
            l_idx = mid_idx + 1
        elif mid_val > needle:
            r_idx = mid_idx - 1

    return result


print(bin_search([1,2,3,4,5,6], 3))
print(bin_search([1,2,3,4,5,6], 6))
print(bin_search([1,2,3,4,5,6], -1))
print(bin_search([1], 1))
print(bin_search([], 1))