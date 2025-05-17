
import time 
import random 

def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        j = i - 1

        while j>=0 and arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            j -= 1 

    return arr 

def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(n-i-1):
            if arr[j+1] < arr[j]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr 

def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        minimum = i
        
        for j in range(i+1, n):
            if arr[minimum] > arr[j]:
                minimum = j 

        if minimum != i:
            arr[minimum], arr[i] = arr[i], arr[minimum]

    return arr 

def merge(arr, left, right, mid):
    n1 = mid - left + 1 # The size of the left array
    n2 = right - mid # the size of the right array 

    L, R = [0] * n1, [0] * n2# temporary arrays 

    # copy data
    for i in range(n1):
        L[i] = arr[left + i]

    for j in range(n2):
        R[j] = arr[mid + 1 + j]

    i, j, k = 0, 0, left

    # Merge the two subarrays in a sorted fashion
    while (i < n1 and j < n2):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1 
        else:
            arr[k] = R[j]
            j += 1 
        k += 1 
    
    # insert remaining data:
    while (i < n1):
        arr[k] = L[i]
        i += 1 
        k += 1 

    while (j < n2):
        arr[k] = R[j]
        j += 1 
        k += 1 

    return arr

def merge_sort(arr, left, right):
    if left < right:
        mid = left + (right - left) // 2

        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)

        return merge(arr, left, right, mid) 

def loop():
    while True:
        while True:
            try:
                option = int(input("Enter an option:\n(1. Insertion sort)\n(2. Bubble sort)\n(3. Selection sort)\n(4. Merge Sort)\n"))
            except ValueError:
                print("Please enter a valid number between 1 and 4\n") 
            else:
                break

        if option == 1:
            time.sleep(1)
            arr = random.sample([1,2,3,4,5,6,7,8,9,11,13,17,19,23,29,31], 8)
            print("Our array:", arr)
            time.sleep(0.7)
            print("Sorting...")
            time.sleep(0.5)
            arr = insertion_sort(arr)
            print("Sorted! Our array now:\n", arr)
            print("The time complexity is O(n^2) in the worst and average case, and for the best is O(n),\nwhere the array is already sorted.")
            time.sleep(1)
            print("And for the space complexity, it's O(1), making it memory efficient, but not\ngood for large datasets.")
            print("\n")
            print("Would you like to continue?")
            nxt = input().lower()
            if nxt == "y" or nxt == "yes":
                continue
    
        elif option == 2:
            time.sleep(1)
            arr = random.sample([1,2,3,4,5,6,7,8,9,11,13,17,19,23,29,31], 8)
            print("Our array:", arr)
            time.sleep(0.7)
            print("Sorting...")
            time.sleep(0.5)
            print("Sorted! Our array now:")
            arr = bubble_sort(arr)
            print(arr)
            print("The time complexity is O(n^2) in the worst and average case, and for the best is O(n),\nwhere the array is already sorted.")
            time.sleep(1)
            print("And for the space complexity, it's O(1), making it memory efficient, but not\ngood for large datasets.")
            print("\n")
            print("Would you like to continue?")
            nxt = input().lower()
            if nxt == "y" or nxt == "yes":
                continue

        elif option == 3:
            
            time.sleep(1)
            arr = random.sample([1,2,3,4,5,6,7,8,9,11,13,17,19,23,29,31], 8)    
            print("Our array:", arr)
            time.sleep(0.7)
            print("Sorting...")
            time.sleep(0.5)
            arr = selection_sort(arr)
            print("Sorted! Our array now:\n", arr)
            print("The time complexity is O(n^2) in the worst and average case, and for the best is O(n),\nwhere the array is already sorted.\n")
            time.sleep(1)
            print("And for the space complexity, it's O(1), making it memory efficient, but not\ngood for large datasets.")
            print("\n")
            print("Would you like to continue?")
            nxt = input().lower()
            if nxt == "y" or nxt == "yes":
                continue

        elif option == 4:
            time.sleep(1)
            
            arr = random.sample([1,2,3,4,5,6,7,8,9,11,13,17,19,23,29,31], 8)    
            print("Our array:", arr)
            time.sleep(0.7)
            print("Sorting...")
            time.sleep(0.5)
            arr = merge_sort(arr, 0, len(arr)-1)
            print("Sorted! Our array now:\n", arr)
            print("The time complexity of merge sort is O(n log n) in all 3 cases,\nbecause we're constantly dividing the arrays in half\nuntil we can't anymore, " \
            "then we merge them together, in a sorted order.\nThis makes this sorting algorithm a divide and conquer algorithm, and is largely used in big datasets")
            time.sleep(3)
            print("And for the space complexity, it's O(n).\nThis is because it uses an auxiliary array of size n to merge sorted halves of the input array.")
            time.sleep(3)
            print("Also, this is my favorite sorting algorithm :>")
            print("\n")
            time.sleep(3)
            print("Would you like to continue?")
            nxt = input().lower()
            if nxt == "y" or nxt == "yes":
                continue

        else:

            print("Nope! Select a valid number")

if __name__ == '__main__':
    loop()