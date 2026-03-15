def merge_sort(arr):
    if len(arr) == 1:
        return arr
    left_arr =  arr[:len(arr)//2]
    right_arr = arr[len(arr)//2:]
    return merge(merge_sort(left_arr), merge_sort(right_arr))

def merge(left_arr, right_arr):
    merge_arr = []
    curr_left_idx = 0
    curr_right_idx = 0
    while curr_left_idx < len(left_arr) and curr_right_idx < len(right_arr):
        left_number = left_arr[curr_left_idx]
        right_number = right_arr[curr_right_idx]
        if left_number < right_number:
            merge_arr.append(left_number)
            curr_left_idx += 1
        else:
            merge_arr.append(right_number)
            curr_right_idx += 1
    merge_arr.extend(left_arr[curr_left_idx:])
    merge_arr.extend(right_arr[curr_right_idx:])
    return merge_arr

arr = [1,2,3,4,5,6,7,8,9,10]
print(merge_sort(arr))