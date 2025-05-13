
#Insertion sort algorithm:
"""

"""

def swap(a, b):
    a, b = b, a
    return a, b
    
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