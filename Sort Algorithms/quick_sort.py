#Its a divide and conquer algorithm
# A pivot is selected, the arrays are then partitioned into sub-arrays.
# According to wheather the sub array is less than or greater than the pivot, they are sorted recursively

def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


arr = [7, 2, 4, 0, 1, 5, 8, 3, 2, 0]
print(quick_sort(arr)) # [0, 0, 1, 2, 2, 3, 4, 5, 7, 8]