
## Selection sort algorithm:

"""
The idea is very simple.

We let n be the length of our array, then we use a for
loop n times starting from one to n, and with index i, then for each iteration,
we acces the current item in our array by i, and set it to the minimum.
Inside our for loop, we loop in the range from i to n, then if our current item 
in the array is less than minimum, we set that item to be the minimum, and we 
swap the those two items.

"""


def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        m = i

        for j in range(i, n):
            if arr[j] < arr[m]:
                m = j
            
            if m != i:
                arr[m], arr[i] = arr[i], arr[m]
    
    return arr

import random 

def generate_array(n):
    arr = random.sample([1,2,3,4,5,6,7,8,9], n)

    return arr

arr = generate_array(7)
print(arr)
print(selection_sort(arr))

# The time complexity is O(n^2) in the average, best and worst case.
# The space complexity is O(1), making it memory efficient.

