#The algorithm's time complexity is roughly O(n^2) due to the nested for loop running based off n numbers
#within the list
def selection_sort(lst):
    for i in range(len(lst)):
        min_index = i
        #Finding the index of the smallest element in the unsorted list
        for j in range(i+1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j
        #Perform the swap
        lst[i], lst[min_index] = lst[min_index], lst[i]
    return lst

lst = [9,8,7,6,5,4,3,2,1]
selection_sort(lst)