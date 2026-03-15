#Binary search algorithm implemented by Me

"""
The algorithm runs in O(logn) complexity as with every iteration of search, the size is reduced by half each time
*Important - The algorithm can only be used on a sorted list
"""

lst = [1,2,3,4,5]

def binary_search(lst, target):
    head = 0
    tail = len(lst) - 1
    mid = len(lst) // 2
    while head <= tail:
        if lst[mid] > target:
            tail = mid - 1
            mid = (head+tail) // 2
        elif lst[mid] < target:
            head = mid + 1
            mid = (head+tail) // 2
        else:
            return True
    return False
        