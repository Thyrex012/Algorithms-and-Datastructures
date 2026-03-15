def quick_sort(arr):

    if len(arr) <= 1:
        return arr

    j = 0
    i = -1
    pivot = arr[-1]
    
    while j < len(arr)-1:
        if arr[j] < pivot:
            i  += 1
            arr[j], arr[i] = arr[i], arr[j]
            j += 1
        else:
            j += 1
    arr[-1], arr[i+1] = arr[i+1], arr[-1]
    
    left = arr[:i+1]
    right = arr[i+2:]

    return quick_sort(left) + [pivot] + quick_sort(right)

lst = [8,2,4,7,1,3,9,5]
print(quick_sort(lst))


