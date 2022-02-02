#Its a divide and conquer algo that divides the input array into 
# two halves and then sorts them, they are divided into smallest units possible.
# After sorting is completed, the halves are merged to form a sorted array.
  
def merge_sort(array):
    if len(array)>1:
        midpoint = len(array)//2
        left = array[:midpoint]
        right = array[midpoint:]

        #Merge sort 
        merge_sort(left)
        merge_sort(right)

        l=r=k=0

       # taking the sorted halves data to other temporary arrays
        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                array[k] = left[l]
                l += 1
            else:
                array[k] = right[r]
                r += 1
            k += 1

      #Ensuring every element is added
        while l < len(left):
            array[k] = left[l]
            l += 1
            k += 1

        while r < len(right):
            array[k] = right[r]
            r += 1
            k += 1
            
array = [45,7,8,0]
def printarray(array):
    for i in range(len(array)):
        print(array[i], end=" ")

merge_sort(array)
printarray(array)