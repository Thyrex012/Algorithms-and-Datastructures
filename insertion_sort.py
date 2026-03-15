#The algorithm has a best case of O(n) where the list is already sorted so the while loop runs linearly 
#However the worst case is O(n^2) as we may have to perform n number of swaps for n interations.
def insertion_sort(lst):
    for i in range(1, len(lst)):
        temp_value = lst[i]
        j = i-1
        while j >= 0 and lst[j] > temp_value:
            lst[j+1], lst[j] = lst[j], lst[j+1]
            j -= 1
            print(lst)
    return lst

lst = [90,80,70,60,50]
insertion_sort(lst)