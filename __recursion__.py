def factorial(n):
    if n == 0:
        return 1
    
    return n * factorial(n-1)


def sum(n):
    if n == 0:
        return 0 
    
    return n + sum(n-1)


def fibonacci(n):
    if n == 0:
        return 0 
    
    if n == 1:
        return 1 
    
    return fibonacci(n-1) + fibonacci(n-2)

def print_array(arr, index, n):
    if index == n:
        return 

    print(arr[index])
    print_array(arr, index + 1, n)


def reverse_array(arr, start, end):
    if start >= end:
        return arr 
    
    arr[start], arr[end] = arr[end], arr[start]
    return reverse_array(arr, start + 1, end - 1)


def recursive_binary_search(arr, left, right, target):
    if left > right:
        return -1
    
    mid = (left + right) // 2 

    if arr[mid] == target:
        return mid 
    elif arr[mid] > target:
        return recursive_binary_search(arr, left, mid-1, target)
    else:
        return recursive_binary_search(arr, mid+1, right, target)
    
# Iterative solution:
def merge_sorted_array(left_arr, right_arr):
    result = []
    i = j = 0 

    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            result.append(left_arr[i])
            i += 1
        else:
            result.append(right_arr[j])
            j += 1 
    
    while i < len(left_arr):
        result.append(left_arr[i])
        i += 1

    while j < len(right_arr):
        result.append(right_arr[j])
        j += 1 

    return result 

arr1, arr2 = [1,3], [2, 4, 7]
# Recursive Solution:

class Solution:
    def merge_sorted_arrays(self, left, right, i=0, j=0, arr=None):
        if arr is None:
            arr = [] 

        if i == len(left):
            return arr + right[j:]
        if j == len(right):
            return arr + left[i:]

        if left[i] <= right[j]:
            arr.append(left[i])
            return self.merge_sorted_arrays(left, right, i+1, j, arr)
        
        else:
            arr.append(right[j])
            return self.merge_sorted_arrays(left, right, i, j+1, arr)
        