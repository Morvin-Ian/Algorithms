#This algo works by repeatedly finding the minimum element
#from the unsorted part and putting it at the begining of the array
# The algo uses a sorted and an unsorted array. In every 
#iteration, the minimum element from the unsortd part is moved to the sorted one.

def selection_sort(lst):
    empty_lst = []
    x = len(lst) - 1
    while x>=0:
        for i in range(len(lst)):
            if lst[i] <= lst[0]:
                lst[0],lst[i] = lst[i],lst[0]
                # this part compares the number in first index and numbers after the first index.
        g = lst.pop(0)
        empty_lst.append(g)
        x -= 1
    return empty_lst
    
print(selection_sort([2,3,4,2,1,1,1,2]))
