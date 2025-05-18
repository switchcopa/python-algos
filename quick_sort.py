
def partition(arr, low, high):

    pivot = arr[high]
    i = low - 1 
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i+=1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1

def quick_sort(arr, left, right):
    if left < right:
        pivot_index = partition(arr, left, right)
        quick_sort(arr, left, pivot_index-1)
        quick_sort(arr, pivot_index+1, right)


data = [1, 7, 4, 1, 10, 9, -2]
print("Unsorted Array")
print(data)

size = len(data)

quick_sort(data, 0, size - 1)

print('Sorted Array in Ascending Order:')
print(data)