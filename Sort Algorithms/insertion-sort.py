# The array is spilt into two parts, One half is sorted
# while the other one is not. The sorted part contains the 
# first element while the other one contains the rest. 
# The first part of the unsorted is compared to the first sorted one and sorting starts from their.

def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >=0 and key < array[j] :
                array[j+1] = array[j]
                j -= 1
        array[j+1] = key

def printarray(array):
    for i in range(len(array)):
        print(array[i], end=" ") 
  
array = [12, 11, 13, 5, 6]
insertion_sort(array)
printarray(array)
        