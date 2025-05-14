

import random

def generate_arr():
    arr = random.sample(range(1,12), 7)

    return arr 


def bubble_sort(A):
    n = len(A)

    for i in range(n):
        for j in range(i+1, n):
            if A[i] > A[j]:
                A[i], A[j] = A[j], A[i]
    
    return A

arr = [2,8,5,3,9,4,1]
arr2 = generate_arr()
arr3 = generate_arr()
print(bubble_sort(arr))
print(bubble_sort(arr2))
print(bubble_sort(arr3))
