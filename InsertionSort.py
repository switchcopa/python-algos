
#Insertion sort algorithm:
"""
    First, we use a for loop and start from an index, say "i", in the range 1 to n, where n is the length of the array.
Then, inside the loop, what we would do, is set an index j = i-1. This index is going to keep track of our next and 
previous items in our array, so we can swap those items.

We need to set a condition whether to keep swapping or not, and that is, j has to be positive or equal to 0, 
and the item in the array at j, should be greater than the one next to it. 
If the condition is true, we loop until it is false, and we keep swapping those two items, and decrement j by 1.
    
We return the array in the end.

--> Sorry if my explanation wasn't too clear, but here's a pseudo code:

insertion sort(array)
n = length of array 

for each index i in the range 1 to n:
    j = i - 1 

    while j >= 0 and (array at j) > (array at j+1):
        swap array at j, and array at j + 1.
        decrement j by 1 

return the array

################################################

There are many solutions to this online but this is just one I made, and the algorithm is straight forward.

"""

def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        j = i - 1 

        while j >= 0 and arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            j -= 1 

    return arr

import random 

def generate_array(n):
    arr = random.sample([1,2,3,4,5,6,7,8,9], n)

    return arr

arr = generate_array(7)
print("Unsorted array:", arr)
arr = insertion_sort(arr)
print(arr)