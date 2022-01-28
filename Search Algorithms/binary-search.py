# This search algo works by repeatedly dividing
# the list/array into half portions untill they
#  have been narrowed down ito just one


search_array = [12, 45, 66, 788, 78]
x =78


def binarysearch(array, x):
    first_value = 0
    last_value = len(array)-1

    while(first_value <= last_value):
        midpoint = (first_value + last_value)//2
        if array[midpoint] == x:
            return True
        elif x < array[midpoint]:
            last_value = midpoint-1
        else:
            first_value = midpoint+1
        print("No")

binarysearch(search_array,x)



