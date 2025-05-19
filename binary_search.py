
"""
~#< BINARY SEARCH >#~


Binary search is a search algorithm that find a target value 
within an sorted array.

for each iteration, half the values are eliminated, this makes
the algorithm's time complexity O(log n), for sorted arrays of 
course. If the array isn't sorted, it would take more, depending
on the sorting algorithm's efficiency.

In our implementation, we're going to use quick sort, a sorting 
algorithm based on divide and conquer that uses a pivot element,
and partitions the array by placing the pivot element to the correct position,
and all the elements on its left are smaller than all the elements on the 
right. 
We use recursion to apply the same to the partitioned subarrays,
and we stop when there is only one element left in the subarray.
The array is then sorted.

But how about binary search? 
We first start with a lower index 'low', 0 and the last index 'high', say n - 1,
where n is the length of the sorted array. Then, while the lower index is 
less or equal to the higher index, we follow this process:

- Choose a middle index 'mid'. 
- if the array at mid is equal to our target data, we return mid.
- if the array at mid is larger than data, we take the right index,
and put it exactly behind our current middle index. 
- if the array at mid is smaller than data, we take the left index,
and we put it exactly after our middle index.

In the end, if we didn't find anything we return None or -1. (Anything to represent that 
we didn't find the index where out target data is not found)

here's a PseudoCode:

binary_search(arr, target):
    low = 0 
    high = len(arr) - 1 

    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == data:
            return mid 
        elif arr[mid] > data:
            right = mid - 1 
        else:
            low = mid + 1 
        
    return -1
"""

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
     
    for j in range(low, high):
        if (arr[j] <= pivot):
            i += 1 
            arr[j], arr[i] = arr[i], arr[j]

    arr[i+1], arr[high] = arr[high], arr[i+1]

    return i + 1 # return the pivot index 

def quick_sort(arr, low, high):
    if (low < high):
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

    return arr 

def binary_search(arr, data):
    n = len(arr)

    left = 0
    right = n - 1

    if arr[left] == data:
        return left 
    
    if arr[right] == data:
        return right 

    while (left <= right): 
        mid = (left + right) // 2

        if arr[mid] == data:
            return mid 
        elif arr[mid] > data:
            right = mid - 1 
        else:
            left = mid + 1 
        
    return -1 

