#The search is sequential. Every value is checked and in case of a match, 
#a particular value is returned, else the search continues.

import time

search_array = [12, 45, 66, 788, 78]
x =78

start = time.time()
def linearsearch(arr, value):
    for n in range(len(search_array)):
        if search_array[n] == x:
            print(f"The Searched value at index {n}")
        print(-1)

linearsearch(search_array,x)
end = time.time()
print((end-start)*1000)


#C++
# bool linearsearch(int A[], int N, int X) {
#   for (int i=0; i<N; i++) 
#     if (A[i] == X) return true;
#   return false;
# }